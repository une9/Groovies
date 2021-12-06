<template>
  <div>
      <carousel id="carousel" :carouselItems="carouselItems"></carousel>
      <search-bar id="home-search-bar"></search-bar>
      <movie-list :movieItems="recommendations"></movie-list>
  </div>
</template>

<script>
import Carousel from '../components/Carousel.vue'
import SearchBar from '../components/SearchBar.vue'
import MovieList from '../components/MovieList.vue'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
    name: 'Home',
    components: { 
        Carousel, 
        SearchBar, 
        MovieList, 
    },
    props: {
        userId: Number,
    },
    data: function () {
        return {
            recommendations: [],
            carouselItems: [],
        }
    },
    created: function () {
        this.$emit('getUserBasics')
        // 영화 가져오기
        axios.get(`${SERVER_URL}/movies/recommendation/`)
            .then(res => {
                this.recommendations = res.data.recommendations
                this.carouselItems = res.data.carouselItems
            })
            .catch(err => {
                console.log(err)
            })
    },
}
</script>

<style>
    #carousel {
        position: absolute;
        top: -100px;
        width: 100%;
        min-width: 768px;
    }

    #home-search-bar {
        margin-top: 580px;
    }
    
</style>