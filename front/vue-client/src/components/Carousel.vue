<template>
  <div class="carousel">
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel" v-if="carouselItems">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="3" aria-label="Slide 4"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="4" aria-label="Slide 5"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[0]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <div class="movieInfo">
              <h5 v-if="carouselItems[0]">
                {{ carouselItems[0].title }}
              </h5>
              <p v-if="carouselItems[0]" class="carousel-tagline">{{ carouselItems[0].tagline }}</p>
              <p v-if="carouselItems[0]" class="carousel-overview">{{ carouselItems[0].overview }}</p>
              <button @click="openModal(0)" data-bs-toggle="modal" data-bs-target="#staticBackdrop" class="btn btn-primary">상세정보</button>
            </div>
          </div>
        </div>
        <div class="carousel-item" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[1]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <div class="movieInfo">
              <h5 v-if="carouselItems[1]">
                {{ carouselItems[1].title }}
              </h5>
              <p v-if="carouselItems[1]" class="carousel-tagline">{{ carouselItems[1].tagline }}</p>
              <p v-if="carouselItems[1]" class="carousel-overview">{{ carouselItems[1].overview }}</p>
              <button @click="openModal(1)" data-bs-toggle="modal" data-bs-target="#staticBackdrop" class="btn btn-primary">상세정보</button>
            </div>
          </div>
        </div>
        <div class="carousel-item" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[2]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <div class="movieInfo">
              <h5 v-if="carouselItems[2]">
                {{ carouselItems[2].title }}
              </h5>
              <p v-if="carouselItems[2]" class="carousel-tagline">{{ carouselItems[2].tagline }}</p>
              <p v-if="carouselItems[2]" class="carousel-overview">{{ carouselItems[2].overview }}</p>
              <button @click="openModal(2)" data-bs-toggle="modal" data-bs-target="#staticBackdrop" class="btn btn-primary">상세정보</button>
            </div>
          </div>
        </div>
        <div class="carousel-item" v-if="carouselItems">
          <img :src=getPosterPath(carouselItems[3]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <div class="movieInfo">
              <h5 v-if="carouselItems[3]">
                {{ carouselItems[3].title }}
              </h5>
              <p v-if="carouselItems[3]" class="carousel-tagline">{{ carouselItems[3].tagline }}</p>
              <p v-if="carouselItems[3]" class="carousel-overview">{{ carouselItems[3].overview }}</p>
              <button @click="openModal(3)" data-bs-toggle="modal" data-bs-target="#staticBackdrop" class="btn btn-primary">상세정보</button>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img :src=getPosterPath(carouselItems[4]) class="d-block w-100" alt="poster image">
          <div class="carousel-caption d-none d-md-block">
            <div class="movieInfo">
              <h5 v-if="carouselItems[4]">
                {{ carouselItems[4].title }}
              </h5>
              <p v-if="carouselItems[4]" class="carousel-tagline">{{ carouselItems[4].tagline }}</p>
              <p v-if="carouselItems[4]" class="carousel-overview">{{ carouselItems[4].overview }}</p>
              <button @click="openModal(4)" data-bs-toggle="modal" data-bs-target="#staticBackdrop" class="btn btn-primary">상세정보</button>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>


<script>

const POSTER_URL = process.env.VUE_APP_POSTER_URL

export default {
    name: 'Carousel',
    props: {
      carouselItems: Array,
    },
    methods: {
      openModal: function (num) {
        this.$store.dispatch('getMovieDetail', this.carouselItems[num].id)
      },
      getPosterPath: function (carouselItem) {
        if (carouselItem && carouselItem.poster_path) {
          return `${POSTER_URL}/${carouselItem.poster_path}`
        }
      },
    },
    filters: {
      getYear: function (string) {
        return string.slice(0,4)
      }
    },
}
</script>


<style>
  .carousel img {
    height: 700px;
    object-fit: cover;
    filter: brightness(30%);
  }

  .carousel h5 {
    font-family: scd8;
    font-size: 4rem;
    width: 70%;
    word-break: keep-all;
  }

  .carousel-caption {
    padding-bottom: 4rem;
  }

  .movieInfo {
    text-align: left;
  }

  .carousel .release-year {
    font-size: 2rem;
    /* margin-left: -0.75rem; */
  }

  .carousel-tagline {
    font-family: scd6;
    margin: 0.25rem 0;
  }

  .carousel-overview {
    width: 60%;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;

    font-size: 0.9rem;
  }

</style>

