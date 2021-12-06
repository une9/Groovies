<template>
  <div id="CommunityArticleCreate">
    <div id="community-article-create">

      <div class="article-create-input-box">
        <label for="title">제목 <span class="split-bar">|</span></label>
        <input v-model="article.title" type="text" id="title" style="width: 20rem;" placeholder="제목을 입력하세요" class="input-style">
      </div>

      <div id="article-header">
        <div>
          작성자: {{ loginUser.nickname ? loginUser.nickname : loginUser.username }} ({{ loginUser.username }})
        </div>
      </div>

      <div class="article-create-input-box">
        <label for="movie_title">영화 제목 <span class="split-bar">|</span></label>
        <input v-model="article.movie_title" type="text" id="movie_title" placeholder="영화 제목을 입력하세요" class="input-style">
      </div>
      <div class="article-create-input-box">
        <label for="content">내용 <span class="split-bar">|</span></label>
        <textarea v-model="article.content" class="textarea" id="content" placeholder="내용을 입력하세요" rows="10"></textarea>
      </div>
    </div>

    <div id="article-create-footer">
      <button v-if="this.$route.query.article > 0" @click="updateArticle">수정</button>
      <button v-else @click="createArticle" class="btn btn-primary">작성</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const AUTH_JWT_TOKEN = { Authorization : `JWT ${localStorage.getItem('jwt')}`}

export default {
  name: 'CommunityArticleCreate',
  data: function () {
    return {
      article: {
        title: '',
        movie_title: '',
        content: '',
      },
    }
  },
  methods: {
    createArticle: function () {
      axios({
        method: 'post',
        url: `${SERVER_URL}/community/create/`,
        headers: AUTH_JWT_TOKEN,
        data: this.article
      })
        .then((res) => {
          this.$router.push({ name: 'CommunityArticle', params: { article_id: res.data.id }})
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateArticle: function () {
      axios({
        method: 'put',
        url: `${SERVER_URL}/community/${this.$route.query.article}/`,
        headers: AUTH_JWT_TOKEN,
        data: this.article
      })
        .then(res => {
          this.$router.push({ name: 'CommunityArticle', params: { article_id: res.data.id }})
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    // 업데이트인 경우, 게시글 정보 받아오기
    if (this.$route.query.article) {
      axios.get(`http://127.0.0.1:8000/community/${this.$route.query.article}/`)
        .then(res => {
          this.article.title = res.data.title
          this.article.movie_title = res.data.movie_title
          this.article.content = res.data.content
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState([
      'login',
      'loginUser',
    ])
  }

}
</script>

<style>
  #community-article-create {
    width: 70%;
    max-width: 768px;
    margin: 0 auto;
    margin-top: 2rem;
    margin-bottom: 2rem;
    text-align: left;
  }

  #community-article-create label {
    text-align: right;
    margin-right: 0.5rem;
  }

  #community-article-create input {
    font-size: 0.875rem;
    padding: 0.25rem;
    display: block;
  }

  #community-article-create textarea {
    margin: 0;
    border-radius: 4px;
    font-size: 0.875rem;
    padding: 0.25rem;
  }

  .article-create-input-box {
    display: grid;
    grid-template-columns: 6rem 1fr;
  }

  #article-create-footer {
    display: flex;
    justify-content: center;
  }

</style>