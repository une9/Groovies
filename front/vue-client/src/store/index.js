import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    login: false,
    searchKeyword: '',
    selectedMovie: {},
    isMyself: false,
    loginUser: {
      id: '',
      username: '',
      nickname: '',
      profile_path: 0,
    },
  },
  mutations: {
    ON_SEARCH: function (state, searchKeyword) {
      state.searchKeyword = searchKeyword
    },
    RESET_SEARCH_KEYWORD: function (state) {
      state.searchKeyword = ''
    },
    UPDATE_MOVIE_DETAIL: function (state, movieDetail) {
      state.selectedMovie = movieDetail
    },
    GET_USER_INFO: function (state, info) {
      state.loginUser.id = info.id
      state.loginUser.username = info.username
      state.loginUser.nickname = info.nickname
      state.loginUser.profile_path = info.profile_path
    },
    LOGOUT: function (state) {
      state.login = false
      state.loginUser = {
        id: '',
        username: '',
        nickname: '',
        profile_path: 0
      }
    },
    LOGIN: function (state) {
      state.login = true
    },
    UPDATE_IS_MYSELF: function (state, BOOL) {
      state.isMyself = BOOL
    },
  },
  actions: {
    onSearch: function ({ commit }, searchKeyword) {
      console.log('actions:onSearch', searchKeyword)
      commit('ON_SEARCH', searchKeyword)
    },
    resetSearchKeyword: function ({ commit }) {
      commit('RESET_SEARCH_KEYWORD')
    },
    onClickMovieItem: function (context, selectedMovieId) {
      this.getMovieDetail(selectedMovieId)
    },
    getMovieDetail: function({ commit }, movieId) {
      // 영화 정보
      let details = `http://127.0.0.1:8000/movies/${movieId}/`
      let actor = `http://127.0.0.1:8000/movies/${movieId}/actor/`
      let director = `http://127.0.0.1:8000/movies/${movieId}/director/`
      let similar = `http://127.0.0.1:8000/movies/${movieId}/similar/`
      
      const requestDetails = axios.get(details)
      const requestActor = axios.get(actor)
      const requestDirector = axios.get(director)
      const requestSimilar = axios.get(similar)

      axios.all([requestDetails, requestActor, requestDirector, requestSimilar])
        .then(axios.spread((...responses) => {
          const requestDetails = responses[0].data
          const requestActor = responses[1].data
          const requestDirector = responses[2].data
          const requestSimilar = responses[3].data
          const allDetails = {
            ...requestDetails,
            actors: requestActor,
            directors: requestDirector,
            similars: requestSimilar
          }
          commit('UPDATE_MOVIE_DETAIL', allDetails)
        }))
        .catch(err => {
          console.log(err)
        })
      
    },
    getUserInfo: function ({ commit }, info) {
      commit('GET_USER_INFO', info)
    },
    logout: function ({ commit }) {
      commit('LOGOUT')
    },
    login: function ({ commit }) {
      commit('LOGIN')
    },
    updateIsMySelf: function ({commit}, BOOL) {
      commit('UPDATE_IS_MYSELF', BOOL)
    },
  },
  getters: {
    loginUserId: state => {
      return state.loginUser.id
    }
  },
  modules: {
  }
})
