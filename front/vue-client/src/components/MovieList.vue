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
        max-width: 1170px;
        margin: 0 auto;
        list-style-type: none;
        display: grid;
        grid-template-columns: repeat(5, 234px)
    }

    @media (max-width: 1200px) {
        .movieList {
            max-width: 936px;
            grid-template-columns: repeat(4, 234px);
        }
    }

    @media (max-width: 992px) {
        .movieList {
            max-width: 702px;
            grid-template-columns: repeat(3, 234px);
        }
    }

</style>