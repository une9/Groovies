<template>
  <div id="login">
    <div class="page-title">
      <h1>로그인</h1> 
      <div class="line"></div>
    </div>
    <div id="login-form">
      <div id="login-form-input">
        <input type="text" id="username" v-model="credentials.username" class="input-style" placeholder="아이디">
        <input type="password" id="password" v-model="credentials.password" class="input-style" placeholder="비밀번호"
          @keypress.enter="login(credentials)">
      </div>
      <div v-if="error_message" id="error-message">
        {{ error_message }}
      </div>
      <button @click="login(credentials)" class="btn btn-primary">로그인</button>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
    name: 'Login',
    data: function () {
        return {
          credentials: {
            username: '',
            password: '',
          },
          error_message: '',
        }
    },
    methods: {
      login: function () {
        axios.post(`http://127.0.0.1:8000/accounts/api-token-auth/`, this.credentials)
          .then((res) => {
            // 토큰을 로컬 저장소에 저장하기
            localStorage.setItem('jwt', res.data.token)
            
            this.$emit('getUserBasics')
            this.$store.dispatch('login')
            this.$router.push({ name: 'Home' })
          })
          .catch(() => {
            this.error_message = "로그인 정보가 틀렸습니다!"
            this.credentials.password = ''
          })
      }
    },
}
</script>

<style>
  #login-form {
    display: grid;
    grid-template-columns: 11.125rem 5rem;
    justify-content: center;
  }

  #login-form-input > input {
    display: block;
    font-size: 0.875rem;
    padding: 0.25rem;
    width: 11rem;
  }

  #login-form-input > input:first-child {
    margin-bottom: 0.125rem;
  }

  #error-message {
    color: rgb(255, 79, 79);
    grid-column: 1/3;
    grid-row: 2/3;
    margin-top: 1rem;
  }
</style>