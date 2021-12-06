import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Community from '@/views/TheCommunity.vue'
import CommunityArticle from '@/views/TheCommunityArticle.vue'
import CommunityArticleCreate from '@/views/TheCommunityArticleCreate.vue'
import Search from '@/views/TheSearch.vue'
import Signup from '@/views/TheSignup.vue'
import Login from '@/views/TheLogin.vue'
import MovieDetail from '@/views/TheMovieDetail.vue'
import UserProfile from '@/views/TheUserProfile.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/community/create',
    name: 'CommunityArticleCreate',
    component: CommunityArticleCreate
  },
  {
    path: '/community/:article_id',
    name: 'CommunityArticle',
    component: CommunityArticle
  },
  {
    path: '/search/:keyword?',
    name: 'Search',
    component: Search,
    props: true
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/movies/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail 
  },
  {
    path: '/accounts/:userid',
    name: 'UserProfile',
    component: UserProfile,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

// 같은 페이지에서 parameter만 변경할 때 NavigationDuplicated 에러 발생 방지
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(() => {
  });
};

export default router
