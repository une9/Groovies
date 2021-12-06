<template>
  <li class="movieItem" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="onClickMovieItem">
    <img v-if="poster_path" :src="poster_path" alt="thumb" class="poster">
  </li>
</template>

<script>

const POSTER_URL = process.env.VUE_APP_POSTER_URL

export default {
    name: 'MovieItem',
    props: {
      movieItem: Object,
    },
    methods: {
      onClickMovieItem: function () {
        this.$store.dispatch('getMovieDetail', this.movieItem.id)
      },
    },
    computed: {
      poster_path: function () {
        return (this.movieItem && this.movieItem.poster_path) ? `${POSTER_URL}/${this.movieItem.poster_path}` : ''
      }
    }
}
</script>

<style>
  .movieItem {
    list-style-type: none;
    display: inline-block;
    margin: 12px;
    cursor: pointer;
  }

  .movieItem > img {
    height: 300px;
    width: 210px;
    object-fit: cover;
  }

  .modal {
    color: black;
  }
</style>