<template>
  <div class="modal fade" data-backdrop="static" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">

        <!-- header -->
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">
            {{ selectedMovie.title }} ({{ selectedMovie.original_title }})
    
            <!-- cart button -->
            <button :disabled="login == false" @click="toggleCart" class="cart-button" :data-bs-dismiss="ratingModal" :aria-label="ratingClose">
              <img src="@/assets/cart_add_2.svg" v-if="!isAddedToCart" alt="cart_add" class="cart-button-icon">
              <img src="@/assets/cart_remove.png" v-if="isAddedToCart" alt="cart_add" class="cart-button-icon">
            </button>

          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <!-- sub-header -->
        <div class="modal-sub-header">
          <div>
            {{ selectedMovie.release_date | getYear }}년 <span class="split-bar">|</span>
            <span v-if="selectedMovie.runtime">{{ selectedMovie.runtime | convertToTime }}</span> <span class="split-bar">|</span>
            
            <!-- average rate -->
            <span>평점 {{ selectedMovie.vote_average > 0 ? selectedMovie.vote_average : '정보 없음' }}</span>
          </div>

          <div>
            <span class="genre-button" v-for="(genre, index) in splited_genres" :key="index" 
            @click="moveToSearch(genre)" data-bs-dismiss="modal" aria-label="Close">
              {{ genre }}
            </span>
          </div>
        </div>

        <hr style="margin: 1rem; color: rgba(165, 165, 165, 0.5);">
        
        <!-- body -->
        <div class="modal-body">
          <div id="movie-trailer-box" v-if="trailer_src">
            <iframe id="movie-trailer" :src="trailer_src" title="YouTube video player" frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
          </div>
          <div class="movie-info"> 
            <div class="movie-info-left">
              <img :src="poster_path" :alt="selectedMovie.title" class="poster">
              <div class="staffs">
                <div>
                  <span class="movie-info-left-title">감독</span> <span class="split-bar">|</span> {{ selectedMovie.directors | getNames }}
                </div>
                <div>
                  <span class="movie-info-left-title">배우</span> <span class="split-bar">|</span> {{ selectedMovie.actors | getNames }}
                </div>
              </div>
            </div>
            <div v-if="selectedMovie.overview" class="movie-info-overview">
              <h6>줄거리</h6>
              <p>{{ selectedMovie.overview }}</p>
            </div>
          </div>
          <button id="close-button-bottom" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <!-- footer -->
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="moveToDetail" data-bs-dismiss="modal" aria-label="Close">
            상세정보 <img src="@/assets/arrow.png" class="arrow">
          </button>
        </div>


      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const AUTH_JWT_TOKEN = { Authorization : `JWT ${localStorage.getItem('jwt')}`}
const POSTER_URL = process.env.VUE_APP_POSTER_URL
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name: 'MovieModal',
    data: function () {
        return {
          isAddedToCart: false,
          myCart: [],
          ratingModal: '',
          ratingClose: '',
          ratingScore: 0,
        }
    },
    methods: {
      moveToDetail: function () {
        this.$router.push({ name: 'MovieDetail',  params: { movie_id: this.selectedMovie.id }})
      },
      toggleCart: function () {
        if ((this.login == true) && (this.loginUser.id != '')) {
          // 로그인한 사용자면
          axios({
            method: 'post',
            url: `${SERVER_URL}/movies/${this.selectedMovie.id}/cart/`,
            headers: AUTH_JWT_TOKEN
          })
          .then(() => {
            this.updateCartState()
          })
          .catch(err => {
            console.log(err)
          })
        }
      },
      moveToSearch: function (genre) {
        this.$router.push({name: 'Search', params: {keyword: genre}})
        this.$store.dispatch('onSearch', genre)
      },
      updateCartState: function () {
        if ((this.login == true) && (this.loginUser.id != '')) {
          axios({
            method: 'get',
            url: `${SERVER_URL}/accounts/mycart/`,
            headers: AUTH_JWT_TOKEN
          })
          .then((res) => {
            this.myCart = res.status == 204? [] : res.data
            this.isAddedToCart =  this.myCart.map(item => item.id).includes(this.selectedMovie.id) ? true : false
          })
          .catch(err => {
            console.log(err)
          })
        }
      },
      updateLoginState: function () {
        if ((this.login == true) && (this.loginUser.id != '')) {
          //ratings 버튼
          this.ratingModal = ''
          this.ratingClose = ''
        } else {
          //ratings 버튼
          this.ratingModal = 'modal'
          this.ratingClose = 'Close'
        }
      },
      updateStates: function () {
        this.updateLoginState()
        if ((this.login == true) && (this.loginUser.id != '')) {
          this.updateCartState()
        }
      },
    },
    filters: {
      convertToTime: function (num) {
        const hour = parseInt(num / 60)
        const minute = num % 60
        return num ? `${hour}시간 ${minute}분` : ''
      },
      getYear: function (string) {
        return string ? string.slice(0,4) : ''
      },
      getNames: function (arr) {
        if (arr) {
          return arr.map(person => person.name).join(', ')
        }
      },
    },
    computed: {
      ...mapState([
        'selectedMovie',
        'loginUser',
        'login'
      ]),
      trailer_src: function () {
        return this.selectedMovie.trailer_key ? `https://www.youtube.com/embed/${this.selectedMovie.trailer_key}`: ''
      },
      poster_path: function () {
        return this.selectedMovie.poster_path ? `${POSTER_URL}/${this.selectedMovie.poster_path}`: ''
      },
      splited_genres: function () {
        return this.selectedMovie.genres ? this.selectedMovie.genres.split(', ') : []
      },
    },
    watch: {
      loginUser: function () {
        this.updateStates()
      },
      selectedMovie: function () {
        this.updateStates()
      },
    },
    created: function () {
      if (this.selectedMovie.id) {
        this.updateStates()
      }
    }
}
</script>

<style>
  .modal-header, 
  .modal-body, 
  .modal-content,
  .modal-footer {
    background-color: #262626;
    border: none;
  }

  .modal-content {
    box-shadow: 0px 0px 42px rgba(0, 0, 0, 0.75);
  }

  .modal-header,
  .modal-sub-header, 
  .modal-body, 
  .modal-footer,
  .detail-header,
  .detail-sub-header, 
  .detail-body {
    padding: 32px;
  }

  .modal-header,
  .detail-header {
    padding-bottom: 0;
    text-align: left;
    align-items: start;
  }

  .modal-body,
  .detail-body {
    padding-top: 0.5rem;
    padding-bottom: 0;
  }

  .modal-sub-header,
  .detail-sub-header {
    text-align: left;
    font-size: 0.875rem;
    padding-top: 0;
    padding-bottom: 0;
  }

  .modal-sub-header > div:first-child,
  .detail-sub-header > div:first-child {
    padding-bottom: 0.5rem;
  }

  .rating {
    cursor: pointer;
  }

  .genre-button {
    background-color: rgb(112,34,171);
    margin: 0.25rem;
    padding: 0 0.75rem;
    height: 1.75rem;
    line-height: 1.75rem;
    display: inline-block;
    border-radius: 0.875rem;
    cursor: pointer;
  }

  .genre-button:first-child {
    margin-left: 0;
  }

  .detail-star-icon {
    width: 1rem;
    height: 1rem;
    margin: 0.125rem;
  }

  .split-bar {
    margin: 0 0.25rem;
    color: rgba(165, 165, 165, 0.5);
  }

  .modal-title,
  .detail-title {
    font-family: scd6;
    font-size: 1.5rem;
    word-break: keep-all;
  }

  .modal-dialog {
    max-width: 800px;
  }

  div.modal {
    color: white;
  }

  #movie-trailer-box {
    position: relative;
    width: 100%;
    height: 0;
    padding-top: 56.25%;
  }

  #movie-trailer {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 100%;
    height: 100%;
  }

  /* bootstrap override */
  .btn-close {
    opacity: 1;
    background: transparent url('../assets/close.svg') center/1em auto no-repeat;
  }

  .cart-button {
    background-color: transparent;
    border: none;
  }

  .cart-button-icon {
    width: 20px;
    height: 20px;
  }

  .movie-info {
    display: flex;
  }

  img.arrow {
    width: 7px;
    height: 14px;
  }

  .movie-info {
    padding-top: 1rem;
  }

  .movie-info .poster {
    margin-right: 1rem;
    margin-bottom: 1rem;
  }

  .movie-info-left {
    text-align: left;
    font-size: 0.875rem;
  }

  .movie-info-left-title {
    font-family: scd6;
  }

  .movie-info-overview {
    text-align: justify;
    padding-right: 10%;
    word-break: break-all;
  }

  .movie-info-overview > h6 {
    text-align: left;
    font-size: 1.25rem;
    font-family: scd6;
  }

  .movie-info-overview > p {
    margin: 0;
  }

  .staffs {
    margin-right: 1rem;
  }

  .modal-body .staffs {
    width: 210px;
  }

  .poster {
    height: 300px;
    width: 210px;
    object-fit: cover;
  }

  .item > div {
    width: 138px;
    word-break: keep-all;
    text-align: left;
  }

  #close-button-bottom {
    position: absolute;
    bottom: -2rem;
    right: 0.5rem;
    padding: 2rem;
    padding-bottom: 0;
  }


  /* star */
  .cls-1{fill:none;stroke:#fbb03b;stroke-linecap:round;stroke-miterlimit:10;}
  .fullStar {
          fill: #fbb03b;
      }

</style>