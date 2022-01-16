<template>
  <div>
    <div class="page-title" style="margin-bottom: 1.5rem;">
      <h1>{{ (this.$route.params.userid == loginUser.id) ? '마이페이지' : '유저정보' }} </h1>
      <div class="line"></div>
    </div>

    <div id="basic-profile">
      <img v-if="(profile_path !== undefined) && (profile_path !== null) && (profile_path !== '')" :src="require(`@/assets/profile_img_${profile_path}.jpg`)" class="profile" alt="profile_img">
      <div id="article-body">
        <div>닉네임: <span style="font-family:scd5;">{{ nickname }}</span></div>
        <div>아이디: {{ username }}</div>
        <button @click="updateProfile" class="btn btn-secondary" v-if="(this.$route.params.userid == loginUser.id)" style="margin-top: 1rem;">회원정보 수정</button>
      </div>
    </div>
    <hr>
    <div id="user-content-box">

      <div>

        <div>
          <h3>별점을 등록한 영화</h3>
          <ul v-if="ratedMovies" class="profile-movieList">
            <li @click="moveToMovie(ratedMovie.id)" 
            v-for="(ratedMovie, index) in ratedMovies" :key="index" class="item profile-movie-item">
              <img v-if="ratedMovie.poster_path" :src="moviePoster(ratedMovie)" class="poster" alt="poster_img">
              <div>
                {{ ratedMovies ? ratedMovie.title : null }}
              </div>
            </li>
          </ul>
          <div v-else>
            {{ (this.$route.params.userid == loginUser.id) ? '영화에 별점을 등록해 보세요!' : '아직 등록한 별점이 없어요'}}
          </div>
        </div>
        <hr>
        <div>
          <h3>{{ (this.$route.params.userid == loginUser.id) ? '내가' : `${nickname}님이` }} 찜한 영화</h3>
          <ul v-if="cartMovies" class="profile-movieList">
            <li v-for="(cartMovie, index) in cartMovies" :key="index" @click="moveToMovie(cartMovie.id)" class="item profile-movie-item">
              <img v-if="cartMovie.poster_path" :src="moviePoster(cartMovie)" class="poster" alt="poster_img">
              <div>
                {{ cartMovies ? cartMovie.title : null }}
              </div>
            </li>
          </ul>
          <div v-else>
            {{ (this.$route.params.userid == loginUser.id) ? '영화를 카트에 담아보세요!' : '아직 찜한 영화가 없어요'}}
          </div>
        </div>
      </div>
      <hr>
      <div id="articleList">
        <h3>{{ (this.$route.params.userid == loginUser.id) ? '내가' : `${nickname}님이` }} 작성한 게시글</h3> 
        <ul id="article-list" v-if="articleList && !articleList.message">
          <li class="article-list-item" v-for="(article, index) in articleList" :key="index">
            <span class="article-list-item-title" @click="moveToArticle(article.id)">
            {{ articleList ? article.title : null }}</span>
            <div class="article-time">{{ articleList ? article.created_at : null | convertFormat }}</div>
          </li>
        </ul>
        <div v-else>
          {{ (this.$route.params.userid == loginUser.id) ? '커뮤니티에 게시글을 작성해보세요!' : '아직 작성한 게시글이 없어요'}}
        </div>
      </div>
      <hr>
      <div id="commentList">
        <h3>{{ (this.$route.params.userid == loginUser.id) ? '내가' : `${nickname}님이` }} 남긴 영화 한마디</h3> 
        <ul id="article-list" v-if="commentList">
          <li class="article-list-item" v-for="(comment, index) in commentList" :key="index">
            <span class="article-list-item-title" @click="moveToMovie(comment.movie)">
            {{ commentList ? comment.content : null }}</span>
            <div>{{ commentList ? findCommentMovie(comment.movie) : null }}</div>
          </li>
        </ul>
        <div v-else>
          {{ (this.$route.params.userid == loginUser.id) ? '영화에 한마디를 남겨보세요!' : '아직 남긴 영화 한마디가 없어요'}}
        </div>
      </div>
    </div>
    <div>
      <a @click="deleteAccount" href="#" class="link-button" v-if="(this.$route.params.userid == loginUser.id)">회원탈퇴</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const POSTER_URL = process.env.VUE_APP_POSTER_URL

export default {
  name: 'UserProfile',
  data: function () {
    return {
      userId: this.$route.params.userid,
      username: '',
      nickname: '',
      profile_path: '',
      ratedMovies: null,
      cartMovies: null,
      articleList: null,
      commentList: null,
    }
  },
  methods: {
    deleteAccount: function () {
      axios.delete(`${SERVER_URL}/accounts/profile/${this.userId}/delete/`)
        .then(() => {
          this.$store.dispatch('logout')
        })
        .then(() => {
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateProfile: function () {
      this.$router.push({ name: 'Signup' })
    },
    moviePoster: function (movie) {
      return `${POSTER_URL}/${movie.poster_path}`
    },
    findCommentMovie: function (movie_id) {
      axios.get(`${SERVER_URL}/movies/${movie_id}/`)
        .then(res => {
          return res.data.title
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToMovie: function (movie_id) {
      this.$router.push({ name: 'MovieDetail', params: { movie_id: movie_id }})
      this.$router.go()
    },
    moveToArticle: function (article_id) {
      this.$router.push({ name: 'CommunityArticle', params: { article_id: article_id }})
    },
  },
  created: function () {
    const createAxios = (url) => {
      return axios({
        method: 'get',
        url: url,
        headers: { Authorization : `JWT ${localStorage.getItem('jwt')}`},
      })
    }
    
    const userInfo = () => createAxios(`${SERVER_URL}/accounts/profile/${this.userId}/`)                 // 유저 정보
    const moviesInCart = () => createAxios(`${SERVER_URL}/accounts/mycart/${this.userId}/`)             // 찜한 영화 리스트
    const ratedMovies = () => createAxios(`${SERVER_URL}/accounts/myrated/${this.userId}/`)             // 평점을 남긴 영화 리스트
    const writtenArticles = () => createAxios(`${SERVER_URL}/accounts/myarticles/${this.userId}/`)      // 작성한 게시글
    const writtenComments = () => createAxios(`${SERVER_URL}/accounts/mycomments/${this.userId}/`)      // 남긴 한줄 댓글

    axios.all([userInfo(), moviesInCart(), ratedMovies(), writtenArticles(), writtenComments()])
    .then(axios.spread((userInfoResp, moviesInCartResp, ratedMoviesResp, writtenArticlesResp, writtenCommentsResp) => {
      // userInfo
      this.username = userInfoResp.data.username
      this.nickname = userInfoResp.data.nickname ? userInfoResp.data.nickname : '(없음)'
      this.profile_path = userInfoResp.data.profile_path

      this.cartMovies = moviesInCartResp.data
      this.ratedMovies = ratedMoviesResp.data
      this.articleList = writtenArticlesResp.data
      this.commentList = writtenCommentsResp.data
    }))
    .catch((error) => {
      console.error(error)
    })
  },
  filters: {
    convertFormat: function (string) {
      return string? `${string.slice(0,4)}년 ${string.slice(5,7)}월 ${string.slice(8,10)}일 ${string.slice(11,16)}` : ''
    },
  },
  computed: {
    ...mapState([
      'login',
      'loginUser',
    ]),
  },
  watch: {
    $route (to, from){
        if (to.name == 'UserProfile' && from.name == 'UserProfile' && to.params.userid !== from.params.userid) {
          this.$router.go()
        }
    }
  },
}
</script>

<style>
  #user-content-box {
    width: 70%;
    margin: 0 auto;
  }

  #basic-profile > img {
    margin: 0;
    margin-bottom: 1rem;
  }

  h3 {
    font-size: 1.5rem;
  }

  .profile-movieList {
        padding: 0;
        max-width: calc(690px + 5rem);
        margin: 0 auto;
        list-style-type: none;
        display: grid;
        grid-template-columns: repeat(5, calc(138px + 1rem));
    }

    @media (max-width: 1200px) {
        .profile-movieList {
            max-width: calc(552px + 4rem);
            grid-template-columns: repeat(4, calc(138px + 1rem));
        }
    }

    @media (max-width: 992px) {
        .profile-movieList {
            max-width: calc(414px + 5rem);
            grid-template-columns: repeat(3, calc(138px + 1rem));
        }
    }

  .item {
    display: inline-block;
    margin: 0.25rem;
  }

  .item.profile-movie-item {
    cursor: pointer;
    margin-bottom: 1rem;
  }

  .link-button {
    color: gray; 
    display: inline-block; 
    margin-top: 4rem;
  }

  .link-button:hover {
    color: white;
  }


</style>