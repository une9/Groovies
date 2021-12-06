<template>
  <div id="app">
    <div id="nav">
      <div>
        <router-link :to="{ name: 'Home' }" :userId="userId"><img src="@/assets/logo.png" alt="logo" class="mainlogo"></router-link> |
        <router-link :to="{ name: 'Search' }">영화 검색</router-link> |
        <router-link :to="{ name: 'Community' }" :login="login">커뮤니티</router-link>
      </div>

      <div v-if="!login">
        <router-link :to="{ name: 'Signup' }">회원가입</router-link> |
        <router-link :to="{ name: 'Login' }">로그인</router-link>
      </div>

      <div v-if="login == true" id="greeting">
        <b>{{ loginUserNickname }}</b>님 환영합니다.
      </div>
      <div v-if="login">
        <router-link v-if="login == true" :to="{ name: 'UserProfile', params: { userid: userId }}">마이페이지</router-link> |
        <router-link to="#" @click.native="logout">로그아웃</router-link>
      </div>

    </div>
    <router-view id="content" @getUserBasics="getUserBasics"/>
    <div id="footer"></div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'App',
  data: function () {
    return {
      userId: '',
    }
  },
  methods: {
    logout: function () {
        localStorage.removeItem('jwt')
        localStorage.removeItem('profilepath')
        this.$store.dispatch('logout')
        this.$router.push({ name: 'Home' })
        this.$router.go()
    },
    // 현재 로그인한 유저 정보 받기
    getUserBasics: function () {
        if (localStorage.getItem('jwt')) {
        const JWTtoken = localStorage.getItem('jwt')
        const base64Payload = JWTtoken.split('.')[1]; //value 0 -> header, 1 -> payload, 2 -> VERIFY SIGNATURE 
        const payload = Buffer.from(base64Payload, 'base64'); 
        const result = JSON.parse(payload.toString()) 
        this.userId = result.user_id
        this.getUserInfo()
      }    
    },
    getUserInfo: function () {
      axios.get(`${SERVER_URL}/accounts/profile/${this.userId}/`)
      .then((res) => {
        this.$store.dispatch('getUserInfo', res.data)
        return res
      }) 
      .catch(err => {
        console.log(err)
      })
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.$store.dispatch('login')
      this.getUserBasics()
      this.getUserInfo()
      localStorage.setItem('profilepath', this.loginUser.profile_path)
    }
  },
  computed: {
    ...mapState([
      'login',
      'loginUser'
    ]),
    loginUserNickname: function () {
      const nickname = this.loginUser.nickname
      return nickname ? nickname : this.loginUser.username
    },
    // loginUserInfo: function () {
    //   return this.$store.state.loginUser
    // },
  },
  watch: {
    $route (to, from){
        if (to.name == 'Search' && from.name == 'Home') {
          this.$store.dispatch('onSearch', this.$route.params.keyword) 
        }
        if (to.name == 'UserProfile') {
          this.$store.dispatch('updateIsMySelf', this.$store.getters.loginUserId == Number(this.$route.params.userid))
        }

    }
  },
}
</script>


<style>
@font-face {
     font-family: 'scd8';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-8Heavy.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

@font-face {
     font-family: 'scd6';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-6Bold.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

@font-face {
     font-family: 'scd3';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

@font-face {
     font-family: 'scd5';
     src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-5Medium.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

.input-style {
  border-radius: 4px;
  border: 1px solid black;
}

/* override bootstrap */
.btn-primary, .btn-primary:hover, .btn-primary:active, .btn-primary:visited {
    background-color: rgb(112,34,171) !important;
    border-color: rgb(112,34,171) !important;
}

/* override bootstrap */
.btn-check:focus + .btn, .btn:focus {
  outline: 0;
  box-shadow: 0 0 0 0.25rem rgb(112,34,171, 0.5) !important;
}

/* override bootstrap */
.btn-check:focus + .btn-primary, .btn-primary:focus {
  color: #fff;
  background-color: rgb(112,34,171) !important;
  border-color: rgb(112,34,171) !important;
  box-shadow: 0 0 0 0.25rem rgb(112,34,171, 0.5) !important;
}

/* override bootstrap */
textarea:hover, 
input[type="text"]:hover, 
input[type="text"]:active, 
input[type="text"]:focus,
input[type="password"]:hover, 
input[type="password"]:active, 
input[type="password"]:focus,
textarea:active, 
textarea:focus, 
button:focus,
button:active,
button:hover,
label:focus,
.btn:active,
.btn.active
{
    outline: none !important;
    -webkit-appearance:none;
    box-shadow: none !important;
}

.logo {
  width: 224px;
  height: 61px;
  margin: 80px;
}

.mainlogo {
  width: 168px;
  height: 45px;
}

body {
  background-color: #262626;
}

#app {
  font-family: scd3, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;

  display: flex;
  flex-direction: column;
  min-height: 100vh;
  min-width: 768px;
}

#nav {
  box-sizing: border-box;
  display: flex;
  justify-content: space-between;
  position: absolute;
  top: 0;
  width: 100%;
  min-width: 768px;
  padding: 32px;
  z-index: 100;
  color: white;
  text-decoration: none;
}

#nav > div {
  display: flex;
  align-items: center;
}

#nav a {
  color: white;
  text-decoration: none;
  display: inline-block;
  margin: 0 1rem;
}

#nav a.router-link-exact-active {
  font-weight: bold;
}

#content {
  margin-top: 100px;
  margin-bottom: 48px;
}

#footer {
  height: 12px;
  width: 100%;
  margin-top: 64px;

  margin-top: auto;

  background : -moz-linear-gradient(87.91% -1117.2% -150deg,rgba(43, 156, 215, 1) 0%,rgba(70, 109, 198, 1) 34.74%,rgba(100, 55, 179, 1) 78.25%,rgba(112, 34, 171, 1) 99.44%);
  background : -webkit-linear-gradient(-150deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  background : -webkit-gradient(linear,87.91% -1117.2% ,12.09% 1217.2% ,color-stop(0,rgba(43, 156, 215, 1) ),color-stop(0.3474,rgba(70, 109, 198, 1) ),color-stop(0.7825,rgba(100, 55, 179, 1) ),color-stop(0.9944,rgba(112, 34, 171, 1) ));
  background : -o-linear-gradient(-150deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  background : -ms-linear-gradient(-150deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#2B9CD7', endColorstr='#7022AB' ,GradientType=0)";
  background : linear-gradient(240deg, rgba(43, 156, 215, 1) 0%, rgba(70, 109, 198, 1) 34.74%, rgba(100, 55, 179, 1) 78.25%, rgba(112, 34, 171, 1) 99.44%);
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#2B9CD7',endColorstr='#7022AB' , GradientType=1);
}

@media screen and (max-width: 992px) {
  #nav > #greeting {
    display: none;
  }
}
</style>
