<template>
  <div id="CommunityArticle">
    <div id="community-article">
      <div id="article-body">
        <h1>{{ article.title }}</h1>
        <div id="article-header">
          <div>
            <img v-if="article.profile_path >= 0" :src="require(`@/assets/profile_img_${article.profile_path}.jpg`)" 
            class="profile-img" alt="profile_img">
            <span class="article-list-item-user" @click="moveToUserProfile(article.user)">{{ article.nickname }}</span>
          </div>
          <div>
            <p>작성  |  {{ article.created_at | convertFormat }}</p>
            <p>수정  |  {{ article.updated_at | convertFormat }}</p>
          </div>
        </div>
        <div id="article-content-box">
            <div id="article-content-btn-box">
              <button @click="updateArticle(article)" v-if="((login == true) && (article.user == loginUser.id))" class="btn btn-secondary article-button">수정</button>
              <button @click="deleteArticle(article)" v-if="((login == true) && (article.user == loginUser.id))" class="btn btn-secondary article-button">삭제</button>
            </div>
          <div v-if="article.movie_title">
            <p>영화: <b>《 {{ article.movie_title }} 》</b></p>
          </div>

          <p id="article-content" style="white-space:pre;">
            {{ article.content }}
          </p>
        </div>
      </div>

        <button v-if="login == true" id="like-button" @click="toggleLike">
          <i class="fa-heart" :class="[{ fas: likeState }, { far: !likeState }]"></i>
          <span>{{likeUsersCount}}</span>
        </button>
        <button v-else id="like-button" @click="toggleLike" disabled>
          <i class="fa-heart far"></i>
          <span>{{likeUsersCount}}</span>
        </button>
        
        <comment 
        :comments="comments"
        :targetId="article.id"
        :targetPage="'community'"
        ></comment>

    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import Comment from '@/components/Comment.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const AUTH_JWT_TOKEN = { Authorization : `JWT ${localStorage.getItem('jwt')}`}

export default {
    name: 'CommunityArticle',
    components: { Comment },
    data: function () {
      return {
        article: {},  // 게시글 정보 + 유저 id (as 'user), username, nickname, profile_path
        comments: [],
        likeState: false,
        likeUsersCount: 0,
      }
    },
    methods: {
      moveToUserProfile: function (user_id) {
        this.$router.push({ name: 'UserProfile', params: { userid: user_id }})
      },
      toggleLike: function () {
        if ((this.login == true) && (this.loginUser.id != '')) {
          // 좋아요 정보 저장하기
        axios({
          method: 'post',
          url: `${SERVER_URL}/community/${this.article.id}/like/`,
          headers: AUTH_JWT_TOKEN
        })
          .then(() => {})
          .catch(err => {
            console.log(err)
          })
        // 하트와 좋아요 수 변경
        if ((this.login == true) && (this.loginUser.id != '')) {
          if (this.likeState) {
            this.likeState = false
            if (this.likeUsersCount > 0) {
                this.likeUsersCount--
              }
          } else {
            this.likeState = true
            this.likeUsersCount++
          }
        }
        }
        
      },
      getLikeState: function (article_id) {
        axios({
          method: 'get',
          url: `${SERVER_URL}/community/${article_id}/like/`,
          headers: AUTH_JWT_TOKEN
        })
          .then(res => {
            this.likeState = res.data.liked
            this.likeUsersCount = res.data.count
          })
          .catch(err => {
            console.log(err)
          })
      },
      updateArticle: function (article) {
        this.$router.push({ name: 'CommunityArticleCreate', query: { article: article.id }})
      },
      deleteArticle: function (article) {
        axios({
          method: 'delete',
          url: `${SERVER_URL}/community/${article.id}/`,
          headers: AUTH_JWT_TOKEN
        })
        .then(() => {
          this.$router.push({ name: 'Community' })
        })
        .catch(err => {
          console.log(err)
        })
      },
    },
    created: function () {
      const article_id = this.$route.params.article_id
      // 게시글 내용, 좋아요 수
      axios.get(`${SERVER_URL}/community/${article_id}`)
        .then(res => {
          this.article = res.data
          this.likeUsersCount = res.data.like_article_users.length
        })
        .catch(err => {
          console.log(err)
        })
      // 댓글
      axios.get(`${SERVER_URL}/community/${article_id}/comment/`)
      .then(res => {
        this.comments = res.data
      })
      .catch(err => {
        console.log(err)
      })  
      // 좋아요 상태
      if (localStorage.getItem('jwt')) {
        this.getLikeState(article_id)
      }
    },
    filters: {
      convertFormat: function (string) {
        return string? `${string.slice(0,4)}년 ${string.slice(5,7)}월 ${string.slice(8,10)}일 ${string.slice(11,16)}` : ''
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
  #community-article {
    width: 70%;
    max-width: 768px;
    margin: 0 auto;
  }

  #article-body h1 {
    font-size: 1.25rem;
    font-weight: normal;
    text-align: left;
  }

  #article-header {
    display: flex;
    padding: 1rem 0.5rem;
    border-top: 1px solid rgb(165, 165, 165);
    border-bottom: 1px solid rgb(165, 165, 165);
    margin: 1rem 0;
  }

  #article-header > div:first-child {
    flex-grow: 1;
    text-align: left;
    display: flex;
    align-items: center;
  }

  #article-content-box {
    padding: 0 1rem;
  }

  #article-content {
    text-align: left;
    width: 100%;
  }

  #article-header > div:last-child > p {
    margin-bottom: 0;
  }

  #like-button {
    background-color: transparent;
    height: 2rem;
    width: 4rem;
    border-radius: 1rem;
    border: 1px solid rgb(165, 165, 165);
    color: white;
    margin-top: 4rem;
  }

  .fa-heart {
    color: crimson;
    margin-right: 0.5rem;
  }

  .profile-img {
    width: 30px;
    height: 30px;
    object-fit: cover;
    border-radius: 50%;
    margin-right: 0.5rem;
  }

  #article-content-btn-box {
    text-align: right;
  }

  button.article-button {
    width: 2rem;
    height: 1rem;
    line-height: 1rem;
    font-size: 0.875rem;
    padding: 6px;
    box-sizing: content-box;
  }

  #article-content-btn-box > button:first-child {
    margin-right: 0.5rem;
  }

</style>