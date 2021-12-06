<template>
    <div class="movieListWrapper">
        <movie-modal></movie-modal>
        <ul class="movieList" v-if="movieItems">
            <movie-item v-for="(movieItem, index) in movieItems" :key="index" :movieItem="movieItem">
            </movie-item>
        </ul>
    </div>
</template>

<script>
import MovieModal from '@/components/MovieModal.vue'
import MovieItem from './MovieListItem.vue'

export default {
    name: 'MovieList',
    components: { MovieModal, MovieItem },
    props: {
        movieItems: Array,
    },
}
</script>

<style>
    .movieList {
        padding: 0;
        max-width: 1200px;
        margin: 0 auto;
    }

</style>