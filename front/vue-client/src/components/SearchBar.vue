<template>
  <div id="searchBar">
      <input type="text" id="SearchInput" 
        class="search-bar"
        placeholder="검색어를 입력하세요" 
        :value="searchKeyword" @input="updateInput" 
        @keypress.enter="onSearch">
      <button @click="onSearch" class="search-button">
          <img src="@/assets/search.png" class="search-icon">
      </button>
  </div>
</template>

<script>
export default {
    name: 'SearchBar',
    data: function () {
        return {
            searchKeyword: '',
        }
    },
    methods: {
        onSearch: function () {
            if (this.searchKeyword && (this.searchKeyword !== this.$route.params.keyword)) {
                this.$router.push({ name: 'Search', params: { keyword : this.searchKeyword }})
                .then(() => {
                    const searchInput = document.querySelector('#SearchInput')
                    searchInput.blur()
                })
                .catch((err)=>{
                    console.log(err)
                })
            }
        },
        updateInput: function(event) {
            this.searchKeyword = event.target.value
        }
    },
    created: function () {
        if (/^\/search\//.test(this.$route.path)) {
            this.searchKeyword = this.$store.state.searchKeyword
        }
    },
    watch: {
        '$route.params.keyword': {
        handler(value) {
            const searchInput = document.querySelector('#SearchInput')
            if (searchInput && value) searchInput.value = value
        },
        deep: true,
        immediate: true
      }
    },
    
}
</script>

<style>
    .search-bar {
        width: 36rem;
        height: 3rem;
        padding: 16px;
        border-radius: 1.5rem 1rem 1rem 1.5rem;
        border: 0;
        margin-bottom: 48px;
    }

    .search-icon {
        width: 18px;
        height: auto;
    }

    .search-button {
        position: relative;
        left: -2rem;
        border: none;
        border-radius: 50%;
        background-color: rgb(112,34,171);
        width: 3rem;
        height: 3rem;
    }

</style>