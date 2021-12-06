<template>
  <div id="Comment">
      <div id="article-comments-box">

        <div id="article-comment-title">댓글 ({{comments.length}})</div>
          <ul id="article-comments">
            <li class="article-comment" v-for="(comment, index) in comments" :key="index">
              <div>
                <img :src="require(`@/assets/profile_img_${comment.profile_path}.jpg`)" 
                class="profile-img comment-profile-img" alt="profile_img">
              </div>
              <div class="comment-username">
                {{ comment.nickname }} 
              </div>
              <div class="comment-content">{{ comment.content }}</div>
              <div class="comment-time">
                <div class="comment-created-at">{{ comment.created_at | convertFormat }}</div>
                <div class="comment-created-at">{{ comment.updated_at | convertFormat }}</div>
              </div>
              <button @click="deleteComment(comment)" 
              v-if="((login == true) && (comment.user == loginUser.id))" class="btn btn-secondary article-button">삭제</button>
            </li>
          </ul>
      </div>

      <div id="comment-input-box">
        <textarea v-if="login == true" id="comment-input" placeholder="댓글을 입력해주세요 :)"
        :commentInput="commentInput" @input="onCommentInput" @keypress.enter="createComment"
        ></textarea>
        <textarea v-else id="comment-input" placeholder="댓글을 작성하려면 로그인해주세요!"
        :commentInput="commentInput" @input="onCommentInput" @keypress.enter="createComment" disabled
        ></textarea>
        <button :disabled="login == false" id="comment-button" @click="createComment" class="btn btn-primary">작성</button>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL
const AUTH_JWT_TOKEN = { Authorization : `JWT ${localStorage.getItem('jwt')}`}

export default {
    name: 'Comment',
    props: {
        comments: Array,
        targetId: Number,
        targetPage: String,
    },
    data: function () {
        return {
            commentInput: '',
        }
    },
    methods: {
        onCommentInput: function (event) {
          this.commentInput = event.target.value
        },
        createComment: function () {
            if (this.commentInput) {
              axios({
                method: 'post',
                url: `${SERVER_URL}/${this.targetPage}/${this.targetId}/comment/create/`,
                data: { content: this.commentInput },
                headers: AUTH_JWT_TOKEN
              })
              .then(() => {
                this.$router.go()
              })
              .catch(() => {
                console.log(this.commentInput)
              })

            // reset commentInput
            this.commentInput = ''
            const commentInputElem = document.querySelector('#comment-input')
            commentInputElem.value = ''
          }
        },
        deleteComment: function (comment) {
          axios({
              method: 'delete',
              url: `${SERVER_URL}/${this.targetPage}/${this.targetId}/comment/${comment.id}/`,
              headers: AUTH_JWT_TOKEN
          })
          .then(() => {
              this.$router.go()
          })
          .catch(err => {
              console.log(err)
          })
      },
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
      ]),
    }

}
</script>

<style>


  #article-comments-box {
    margin-top: 3rem;
  }

  #article-comment-title {
    font-family: scd6;
    /* font-size: 1.25rem; */
    text-align: left;
    margin-bottom: 0.25rem;
  }

  #article-comments {
    list-style: none;
    padding: 0;
    border-top: 1px solid white;
    border-bottom: 1px solid white;
    
  }

  .article-comment {
    padding: 2rem 0;
    border-bottom: 1px solid rgb(165, 165, 165);
    display: flex;
  }

  .comment-username {
    font-family: scd6;
    margin-right: 1rem;
  }

  .comment-content {
    flex-grow: 1;
    text-align: left;
    border-left: 1px solid white;
    padding: 0 1rem;
  }

  #article-header > div:last-child,
  .comment-created-at {
    font-size: 0.75rem;
    color: rgb(151, 151, 151);
  }

  .comment-username,
  .comment-content,
  .comment-created-at {
    display: flex;
    align-items: center;
  }

  .comment-time {
    display:flex;
    flex-direction: column;
    margin-right: 1rem;
  }

  #comment-input-box {
    display: flex;
  }

  #comment-input {
    width: 100%;
    height: 4rem;
    resize: none;
    padding: .5rem;
    border: none;
  }

  #comment-button {
    width: 128px;
    height: 4rem;
    border: none;
    border-radius: 0 0.25rem 0.25rem 0;
  }

</style>