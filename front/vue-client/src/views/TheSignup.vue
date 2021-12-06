<template>
  <div id="signup">
    <div class="page-title">
      <h1 v-if="this.login == true">회원 정보 수정</h1> 
      <h1 v-else>회원가입</h1> 
      <div class="line"></div>
    </div>
    <div id="signup-form">
      <!-- profile img select -->
      <div id="profile-img-select-box">
        <p>마음에 드는 프로필 사진을 골라주세요</p>
        <img v-for="(x, idx) in new Array(5)" :key="idx"
        :class="{ click: credentials.profile_path === idx }" 
        @click="setProfilePath(idx)" :src="require(`@/assets/profile_img_${idx}.jpg`)" 
        :alt="`${idx}번_프로필`" class="profile">
      </div>

      <!-- input -->
      <div id="signup-input-box">
        <div id="signup-input-inputs">
            <label class="signup-input-label" for="nickname">닉네임 <span class="split-bar">|</span></label>
            <input v-if="this.login == true" type="text" id="nickname" :value="credentials.nickname" @input="onInputNickname" class="input-style" :class="{ red: !checkValidNickname }" :placeholder="this.$store.state.loginUser.nickname">
            <input v-else type="text" id="nickname" :value="credentials.nickname" @input="onInputNickname" class="input-style" :class="{ red: !checkValidNickname }">
            <div></div>   <!-- 자리 채우기용  -->
            <div class="notice-box">
              <p class="tag" v-if="credentials.nickname" v-show="checkValidNickname">사용 가능한 닉네임입니다.</p>
              <p class="tag invalid" v-if="credentials.nickname" v-show="!checkValidNickname">이미 사용중인 닉네임입니다.</p>
            </div>

            <!-- <input type="text" id="nickname" :value="credentials.nickname" @input="onInputNickname" :class="{ red: checkValidNickname }">
            <p class="tag" :class="{ invalid : checkValidNickname }" v-if="credentials.nickname">{{ nicknameNotice }}</p> -->

            <label class="signup-input-label" for="username">아이디 <span class="split-bar">|</span></label>
            <input v-if="this.login == true" type="text" id="username" :value="loginUser.username" class="input-style" :class="{ red: !checkValidUsername }" readonly disabled>
            <input v-else type="text" id="username" :value="credentials.username" @input="onInputUsername" class="input-style" :class="{ red: !checkValidUsername }">
            <div></div>   <!-- 자리 채우기용  -->
            <div class="notice-box">
              <p class="tag" v-if="credentials.username" v-show="checkValidUsername">사용 가능한 아이디입니다.</p>
              <p class="tag invalid" v-if="credentials.username" v-show="!checkValidUsername">이미 사용중인 아이디입니다.</p>
            </div>

            <!-- <input type="text" id="username" :value="credentials.username" @input="onInputUsername" :class="{ red: checkValidUsername }">
            <p class="tag" :class="{ invalid : checkValidUsername }" v-if="credentials.username">{{ usernameNotice }}</p> -->

            <label class="signup-input-label" for="password">비밀번호 <span class="split-bar">|</span></label>
            <input type="password" id="password" v-model="credentials.password" @input="[checkValidPW(), checkSamePW()]"
            :class="{ red: isInvalidPW }" class="input-style">
            <div></div>   <!-- 자리 채우기용  -->
            <div class="notice-box">
              <p class="tag">* 영문, 숫자를 모두 포함하여 8자리 이상</p>
            </div>

            <label class="signup-input-label" for="passwordConfirmation">비밀번호 확인 <span class="split-bar">|</span></label>
            <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" 
            @input="[checkValidPW(), checkSamePW()]" :class="{ red: isNotSamePW }" class="input-style">
            <div></div>   <!-- 자리 채우기용  -->
            <div class="notice-box">
              <p class="notice invalid" :class="{ shown: isNotSamePW }">비밀번호가 일치하지 않습니다!</p>
            </div>
        </div>

        <div v-if="this.login !== true" class="agree-box">
          <input type="checkbox" id="agree" style="display: none;">
          <label for="agree" style="cursor: pointer;">
            <div id="custom-checkbox" @click="toggleCheckBox"></div>
          </label>
          <label for="agree" style="cursor: pointer;" @click="toggleCheckBox">회원가입에 동의합니다!</label>
        </div>
      </div>

      <button v-if="this.login == true" @click="update" class="btn btn-primary signup-button" :disabled="!isValidForm">회원정보 수정</button>
      <button v-else @click="signup" class="btn btn-primary signup-button" :disabled="!isValidForm">회원가입</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const AUTH_JWT_TOKEN = { Authorization : `JWT ${localStorage.getItem('jwt')}`}

export default {
    name: 'Signup',
    data: function () {
        return {
          credentials: {
            nickname: '',
            username: '',
            password: '',
            passwordConfirmation: '',
            profile_path: null,
          },
          isInvalidPW: false,
          isNotSamePW: false,
          existingUsernames: [],
          existingNicknames: [],
        }
    },
    methods: {
      toggleCheckBox: function () {
        const box = document.querySelector('#custom-checkbox')
        if (box.classList.contains('focus')) {
          box.classList.remove('focus')
        } else {
          box.classList.add('focus')
        }
      },
      onInputNickname: function (event) {
        this.credentials.nickname = event.target.value
      },
      onInputUsername: function (event) {
        this.credentials.username = event.target.value
      },
      signup: function () {
        // console.log('signup!!')
        const agreed = document.querySelector('#agree').checked
        if (this.checkValidUsername && this.checkValidNickname && !this.isInvalidPW && !this.isNotSamePW && agreed) {
          // 회원가입 가능
          axios({
            method: 'post',
            url: `${SERVER_URL}/accounts/signup/`,
            data: {
              profile_path: this.credentials.profile_path,
              nickname: this.credentials.nickname,
              username: this.credentials.username,
              password: this.credentials.password,
              passwordConfirmation: this.credentials.passwordConfirmation
            }
          })
            .then(() => {
              this.$router.push({ name: 'Login' })
            })
            .catch(() => {
              this.$router.go()
            })

        }
      },
      // 프로필 사진
      setProfilePath (num) {
        this.credentials.profile_path = num
        this.clickedImg = num
      },
      // 비밀번호
      checkValidPW: function () {
        if (this.credentials.password.length) {
          if (/^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$/.test(this.credentials.password)) {
            this.isInvalidPW = false
          } else {
            this.isInvalidPW = true
          }
        } else {
          this.isInvalidPW = false
        }
      },
      checkSamePW: function () {
        if (this.credentials.passwordConfirmation.length) {
          if (this.credentials.password !== this.credentials.passwordConfirmation) {
            this.isNotSamePW = true
          } else {
            this.isNotSamePW = false
          }
        } else {
          this.isNotSamePW = false
        }
      },
      getAllUsername: function () {
        axios.get(`${SERVER_URL}/accounts/profile/`)
          .then(res => {
            const userList = []
            for (let i=0; i < res.data.length ; i++) {
              userList.push(res.data[i].username)
            }
            this.existingUsernames = userList
          })
          .catch(err => {
            console.log(err)
          })
      },
      getAllNickname: function () {
        axios.get(`${SERVER_URL}/accounts/profile/`)
          .then(res => {
            const userList = []
            for (let i=0; i < res.data.length ; i++) {
              userList.push(res.data[i].nickname)
            }
            this.existingNicknames = userList
          })
          .catch(err => {
            console.log(err)
          })
      },
      update: function () {
        if (this.credentials.nickname !== '') {
          axios({
            method: 'put',
            url: `${SERVER_URL}/accounts/profile/${this.loginUser.id}/update/`,
            headers: AUTH_JWT_TOKEN,
            data: {
              profile_path: this.credentials.profile_path,
              nickname: this.credentials.nickname,
              password: this.credentials.password,
              passwordConfirmation: this.credentials.passwordConfirmation,
              username: this.loginUser.username
            }
          })
            .then(() => {
              this.$router.push({ name: 'UserProfile', params: { userid: this.loginUser.id }})
            })
            .catch(err => {
              console.log(err)
            })
        } else {
          axios({
            method: 'put',
            url: `${SERVER_URL}/accounts/profile/${this.loginUser.id}/update/`,
            headers: AUTH_JWT_TOKEN,
            data: {
              profile_path: this.credentials.profile_path,
              nickname: this.loginUser.nickname,
              password: this.credentials.password,
              passwordConfirmation: this.credentials.passwordConfirmation,
              username: this.loginUser.username
            }
          })
            .then(() => {
              this.$router.push({ name: 'UserProfile', params: { userid: this.loginUser.id }})
            })
            .catch(err => {
              console.log(err)
            })
        }
        
      },
    },
    created: function () {
      this.getAllUsername()
      this.getAllNickname()
      // console.log(this.loginUser.profile_path)
      this.setProfilePath(this.loginUser.profile_path)
    },
    computed:{
      ...mapState([
        'loginUser',
        'login'
      ]),
      checkValidUsername(){
        if (this.credentials.username.length > 0) {
          let usedUsername = this.existingUsernames.includes(this.credentials.username)
          if (this.existingUsernames.length > 0 && usedUsername) return false
          return true
        } else {
          return true
        }
      },
      checkValidNickname(){
        if (this.credentials.nickname.length > 0) {
          let usedNickname = this.existingNicknames.includes(this.credentials.nickname)
          if (this.existingNicknames.length > 0 && usedNickname) return false
          return true
        } else {
          return true
        }
      },
      isValidForm: function () {
        if (this.credentials.password && this.credentials.passwordConfirmation && (this.credentials.password === this.credentials.passwordConfirmation)) {
          if (this.login == true) return true
          else return this.credentials.username ? true : false
        }
        return false
      },
    },
}
</script>

<style>
  .agree-box ,
  .signup-button {
    margin-top: 1rem;
  }
  #signup-input-box {
    display: grid;
  }

  .signup-input-label {
    display: block;
    text-align: right;
    margin-right: 0.5rem;
  }

  #signup-input-inputs {
    text-align: left;
    display: grid;
    grid-template-columns: 8rem 16rem;
    justify-content: center;
    row-gap: 0.125rem;
  }
  
  #signup-input-inputs input {
    display: block;
  }

  #profile-img-select-box {
    margin-bottom: 4rem;
  }

  #profile-img-select-box > p {
    margin-bottom: 2rem;
  }

  .invalid {
    color: rgb(255, 79, 79);
  }

  .click {
    box-shadow: 0 0 0 0.9rem rgb(112, 34, 171);
  }

  .profile {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 50%;
    margin-right: 2rem;
    cursor: pointer;
  }

  .page-title {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 48px 0 64px 0;
  }

  .page-title > h1 {
    font-family: scd6;
    font-size: 1.75rem;
  }

  .line {
    height: 2px;
    width: 192px;
    background-color: white;
    margin-top: 12px;
  }

  .tag {
    font-size: 0.75rem;
    display: inline-block;
  }

  .notice {
    font-size: 0.75rem;
    display: none;
  }

  .shown {
    display: block;
  }

  input.red {
    border: none;
    background-color: rgb(255, 139, 139);
  }

  #custom-checkbox {
    width: 12px;
    height: 12px;
    background-color: white;
    border-radius: 2px;
    margin-right: 2px;
  }

  #custom-checkbox.focus {
    /* background-color: rgb(112,34,171); */
    background: rgb(112,34,171) url('../assets/check.png')  no-repeat center center;
    background-size: 80%;
  }

</style>