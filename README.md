# 최종 프로젝트

<iframe width="560" height="315" src="https://www.youtube.com/embed/sl8WIdMBYOI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 0. 아키텍처

✔ Django REST API 서버와 Vue.js

- TMDB API 사용

- Django의 secret key를 노출하지 않기 위해 `.secrets.json` 파일로 분리하여 관리한다. 해당 파일은 프로젝트 폴더 안에 위치한다.

  ```json
  {
      "SECRET_KEY": "DJANGO_SECRET_KEY_HERE"
  }
  ```

  ```python
  # settings.py의 SECRET KEY 위치
  import os, json
  from django.core.exceptions import ImproperlyConfigured
  
  
  secret_file = os.path.join(BASE_DIR, 'secrets.json')
  
  with open(secret_file) as f:
      secrets = json.loads(f.read())
  
  def get_secret(setting, secrets=secrets):
      try:
          return secrets[setting]
      except KeyError:
          error_msg = "Set the {} environment variable".format(setting)
          raise ImproperlyConfigured(error_msg)
  
  SECRET_KEY = get_secret("SECRET_KEY")
  ```

- Vue에서 환경 변수를 관리하기 위해  `.env` 파일로 분리하여 관리하며, 이 또한 프로젝트 폴더 안에 위치한다.

  본 프로젝트에서는 서버 url와 포스터 경로 url을 관리하고 있다.

  ```
  VUE_APP_SERVER_URL=http://127.0.0.1:8000
  VUE_APP_POSTER_URL=https://image.tmdb.org/t/p/original
  ```

  

## 1. 팀원 정보 및 업무 분담 내역

### (1) 팀원 정보

서울 4반 9조

- 김민채 (팀장)
- 윤혜구

### (2) 업무 분담 내역

- 공통) 웹 애플리케이션 컨셉 확정, 와이어프레임 설계, ERD 설계, 오류 수정

- 김민채: [Backend] Django 서버, DB 구축, Vue.js에서 비동기 요청을 사용한 JS 작성
- 윤혜구: [Frontend] Vue.js 전반 (CSS 작성 및 컴포넌트 배치 설계), 로고 및 화면 구성 디자인

## 2. 일정

![timeline](README.assets/timeline.png)

- **1일차** (11월 17일 수요일)
  
  - 최종 프로젝트의 시작
  - 팀장 선정, 팀명과 구호 설정, 서비스명("Groovies")과 대표 색상 등 정체성 결정, 공용 노션 생성
  - 프로젝트 컨셉 논의
    - 사이트에 대한 컨셉 회의를 진행했고, 처음에는 명세를 읽는 관점이 달랐다. 웹 애플리케이션의 목적이 영화의 정보를 조회인지, 사용자 맞춤 영화 추천인지에 대해 의견이 갈렸고, 결국 검색을 통한 조회는 필요하지만 상세한 검색은 크게 요구되지 않는다는 점에서 일치를 이뤘음
    - 영화의 상세 정보를 보여줄 때 모달 창의 사용 여부를 논의하였고, 모달 창이 빠른 브라우징을 하는 사용자에게 편리하므로 사용하기로 결정함
    - Figma를 통해 함께 와이어프레임을 설계함
  
  * TMDB API의 데이터를 사용하기로 결정. TMDB의 키워드 검색 기능을 이용하기 위함
  * 예상 결과 화면 제작
- **2일차** (11월 18일 목요일)
  - 와이어 프레임 완성
  - ERD 설계
  - 아키텍처 결정 및 역할 분담: 김민채 백엔드(Django), 윤혜구 프런트엔드(Vue.js)
  - DB 구축 시작
  - 추천 알고리즘 결정
- **3일차** (11월 19일 금요일)
  - DB 구축 실패 (sql 구문 사용 방법)
  - 논의: 관련 영화의 데이터는 수집하지 않는다. 연쇄적으로 가기 때문에 작은 데이터베이스로 감당할 수 없게 된다.
  - Django 기능 구현 완료, Postman으로 응답 확인
  - 모달 데이터 보내주는 구조 짜고 template으로 출력
  - 회원가입, 로그인 input validation (통신 부분 제외 구현) 
  - 스타일 입히기 일부
- **4일차** (11월 20일 토요일)
  - 키워드 검색 기능 구현: 장르, 영화 제목, 영화 원제를 대상으로 필터링
  - 추천 알고리즘 구현
  - 모달 구현
- **5일차** (11월 21일 일요일)
  - 찜하기 기능 구현
  - 프로필 페이지 함수 구현 (찜한 영화, 평점을 남긴 영화, 작성한 영화 한마디, 작성한 게시글을 조회)
  - Vue.js의 JS 작성 시작: 검색 기능 작성, 커뮤니티 기능 구현 시작
  - 검색 기능 완성
  - 커뮤니티 페이지 구성
  - 장고 서버와 Vue.js 연결
- **6일차** (11월 22일 월요일)
  - 커뮤니티 기능 구현: 게시글 목록 조회, 개별 게시글 조회·작성·삭제, 댓글 작성·삭제, 게시글 좋아요
  - 회원가입 기능 구현
  - 로그인 기능 구현
  - 좋아요 기능 수정
  - 캐러셀 디자인 완성, 에러 수정
  - 검색 관련 에러 수정
  - 깃랩에서 받은 vue 서버가 안켜지는 문제 해결
- **7일차** (11월 23일 화요일)
  - 진행상황 공유
  - 회원정보수정 기능 구현
  - serializer 수정
  - 모달 완성
- **8일차** (11월 24일 수요일)
  - 오류 수정
  - 소셜 로그인 기능 구현 시도 → 실패 (Django와 Vue.js를 함께 쓰니 익숙하지 않았고 잘 되지 않음)
  - 중복 코드 정리
  - detail 페이지 완성
  - Comment.vue로 댓글 컴포넌트 분리 후 재사용
- **9일차** (11월 25일 목요일)
  
  - 코드 정리 및 오류 수정
  - 스타일 완성
  - 최종본 완성
  - 발표 자료 작성

## 3. 데이터베이스 모델링 (ERD)

<img src="README.assets/ERD.png" alt="ERD"/>

- Django 앱은 총 3개다: accounts, community, movies
  - accounts 앱: User 모델을 갖고 있으며, 회원가입과 로그인, 좋아요, 평점, 찜하기 기능 등과 관련되어 있다. 각 게시물, 댓글, 찜, 평점에 대하여 사용자 정보가 들어가므로 다른 앱 두 개와 깊은 연관을 맺고 있다.
  - community 앱: Article과 Comment 모델을 갖고 있는, 커뮤니티 기능을 관장하는 앱이다. 커뮤니티 게시글과 댓글을 관리할 수 있다.
  - movies 앱: Movie, Comment, Cart, Rating, Actor, Director, Similar 의 모델을 가진 앱이다. 웹 애플리케이션에서 영화 정보를 보여주고, 영화에 대한 한마디를 받고, 사용자가 영화에 대해 평점과 댓글을 남기고 찜하기를 할 수 있게끔 영화 정보를 제공한다.
- movies 앱에는 기본이 되며 영화 정보를 담고 있는 movie 모델과, 추가 정보를 제공하는 actor, director, similar(관련 영화) 모델이 있다. cart(찜하기), comment(영화 한마디), rating(평점) 모델은 accounts앱의 user 모델과 관계를 형성하고 있으며, 각 모델은 user와 movie를 외래키로 가진다.
- community 앱에는 article과 comment 모델이 있고, 이들 모델 또한 accounts 앱의 user 모델과 관계를 형성한다. (작성자가 있어야 하므로!)
- 또한, 영화 한마디에 좋아요를 누른 사람을 조회하기 위한 테이블과 게시글에 좋아요를 누른 사람을 조회하기 위한, 다대다 관계용 테이블이 만들어졌다.



## 4. 목표 서비스 구현 및 실제 구현 정도

### (1) 와이어프레임 (초기 목표)

- #### 메인 화면, 검색 화면

  <img src="README.assets/wireframe_1.png" alt="wireframe_1" style="zoom:25%;" />

  - **메인 페이지**

    유명한 OTT 서비스들처럼, 메인 화면에서는 추천 영화의 포스터를 크게 보여주면서 사용자의 이목을 집중시키고 몰입감을 향상시킨다. carousel로 구현되어 일정 시간이 지나면 다음 포스터로 넘어가게 된다. 

    아래에는 검색창과 카테고리별 영화들이 나열되어 있다. 검색창에서는 키워드를 입력하여 관련된 영화를 찾을 수 있고, 검색 결과는 검색 페이지에 표시된다.

    카테고리 별 영화는 사용자별 추천 영화, 인기 영화, 최신 영화, 그리고 평균 평점이 높은 영화로 분류하여 제시된다.

  - **검색 페이지**

    메인 페이지의 검색창을 이용할 수도 있고, 화면의 라우터 링크를 통해 검색 페이지로 이동하여 검색을 진행할 수도 있다. 검색 키워드를 입력하면 해당 키워드를 영화 제목, 영화 내용, 영화에 등록된 키워드 목록에서 조회하여 일치하는 영화들을 나열한다.

    왼쪽 사이드바에서는 장르, 러닝타임, 그리고 별점에 대한 필터를 적용하여 사용자가 원하는 특징을 가진 영화들을 손쉽게 검색하여 알아낼 수 있다.

    

- #### 영화 정보 모달 창, 영화 상세정보 페이지

  <img src="README.assets/wireframe_2.png" alt="wireframe_2" style="zoom: 25%;" />
  - **영화 정보 모달 창**

    메인 페이지의 영화 목록에서 영화를 클릭하거나, 검색 페이지에서 영화를 클릭했을 때, 해당 영화의 상세정보 페이지로 이동하기 전, 기본적인 정보들을 간략하게 보여주는 창이다. 사용자는 해당 페이지를 쉽게 켜고 끌 수 있는 화면 전환이 용이하므로 여러 영화를 둘러볼 때 유용한 형태이다. 

    상단에는 해당 영화의 트레일러 영상을 넣고, 아래쪽에는 포스터와 간략한 줄거리를 소개한다. 더 많은 정보를 보고 싶으면 아래쪽의 '상세정보 보러가기'를 클릭함으로써 영화 상세정보 페이지로 이동할 수 있다.

  - **영화 상세정보 페이지**

    모달 페이지에 담지 못했던 세부적인 정보가 담긴 페이지로, 출연진과 감독, 관련 영화 목록이 나오며, 아래쪽에는 사용자들이 영화에 대한 한마디를 나눌 수 있는 공간이 마련되어 있다. 사용자들은 영화에 대해 별점으로 의견을 표시할 수 있으며, 또한 댓글을 남기거나 기존 댓글에 좋아요를 누름으로써 생각을 공유할 수 있다.

- #### 프로필 페이지, 회원정보 수정 창

  <img src="README.assets/wireframe_3.png" alt="wireframe_3" style="zoom:25%;" />

  - **프로필 페이지**

    사용자들의 자신의 프로필을 관리할 수 있는 공간이다. 닉네임과 아이디 그리고 프로필 사진 등의 개인정보가 기재되어 있다. 아래쪽에는 사용자의 활동 내역이 표시되는데, 사용자가 평점을 등록한 영화, 찜하기를 눌러 보고 싶음을 표시한 영화, 영화에 작성한 한마디, 그리고 커뮤니티에 작성한 게시글을 한데 모아서 볼 수 있다. 아래쪽에는 회원탈퇴 링크가 위치해 있다.

  - **회원정보 수정 창**

    프로필 페이지에서 회원 정보 수정 버튼을 클릭하면 해당 창이 뜨면서 사용자가 개인의 프로필을 수정할 수 있다. 아이디는 한 명의 사용자에 하나로 제한되어 있어 변경이 불가하지만, 프로필 사진을 비롯해 닉네임과 비밀번호를 변경할 수 있다.

- #### 로그인 창, 회원가입 창

  <img src="README.assets/wireframe_4.png" alt="wireframe_4" style="zoom:25%;" />
  - **로그인 창**

    사용자가 로그인을 할 수 있는 창이다. 아이디와 비밀번호를 사용하여 로그인한다.

  - **회원가입 창**

    새 사용자가 회원으로 가입할 수 있는 창이다. 처음에 별명과 아이디를 설정하게 되며, 아이디는 중복 여부를 확인하여 알려준다. 비밀번호 확인란을 통해 비밀번호를 제대로 입력했는지 검사한다. 서버 쪽에서도 재차 검사한다. '동의합니다.'에 대한 체크 버튼을 만들어 사용자의 회원가입을 확인하는 용도로 사용한다.

* #### 예상 결과 화면

  ![main](README.assets/main.png)

  ![modal_detail](README.assets/modal_detail.png)

  * 앞서 작성한 와이어프레임을 바탕으로 실제 결과물이 어떤 느낌일지 파악하고 로고 디자인과 메인 컬러 등을 결정하기 위해 실제 예상 결과물의 모습을 간단하게 구현했다. 
    * 이후 논의 끝에 주제별로 나뉘어 있던 추천영화 칸이 하나로 합쳐지게 되었다.

<br/>

### (2) 실제 구현

#### 1) Vue.js 구조

<img src="README.assets/image-20211125194302087.png" alt="image-20211125194302087" style="zoom:150%;" />



#### 2) 구현 결과 이미지

- ##### 메인 페이지
  - router-link로 검색, 커뮤니티, 회원가입, 로그인 페이지로 이동할 수 있다. 로그인이 된 사용자라면 회원가입과 로그인 대신, 마이페이지와 로그아웃에 대한 경로를 보게 된다.
  - 캐러셀로 영화 포스터, 제목, 부제가 보여지며, 상세정보 버튼을 통해 모달 창을 띄울 수 있다.
  - 영화 목록은 추천 알고리즘을 통해 제시되었으며, 영화 포스터를 누르면 모달 창을 볼 수 있다.

<img src="README.assets/mainpage.png" alt="mainpage" style="zoom:50%;" />

- ##### 영화 정보 모달 창

  - 트레일러와 함께, 포스터와 줄거리 등 간략한 정보를 볼 수 있다. 아래쪽의 상세정보 버튼을 통해 상세 페이지로 이동할 수 있으며, 오른쪽 상하단의 'x' 표로 모달 창을 나갈 수 있다.

<img src="README.assets/modalpage.png" alt="modalpage" style="zoom:50%;" />

- ##### 영화 세부정보 페이지
  - 영화에 대한 보다 자세한 정보가 나오며, 제목 옆의 '+' 버튼을 통해 찜하기를, 별점을 누름으로써 평점 주기를, 아래쪽에 댓글 작성을 통해 영화 한마디를 남길 수 있다.

<img src="README.assets/details.png" alt="details" style="zoom:50%;" />

- ##### 검색 페이지

  - 검색 키워드를 장르 또는 제목 또는 원제에 가지고 있다면 결과로 뜨게 된다. 여기서도 포스터를 클릭하여 영화에 대한 모달 창을 띄울 수 있다.

<img src="README.assets/search.png" alt="search" style="zoom:50%;" />

- ##### 커뮤니티 페이지

  - 로그인을 하지 않았다면 로그인을 해달라는 문구와 함께 로그인 버튼이 생긴다. 

  - 게시글이 없으면, 작성 버튼과 함께 첫 게시글을 남겨달라는 문구가 뜨며, 게시글이 있으면 생성시간 순으로 게시글의 제목 목록이 나오게 된다.

  - 게시글을 클릭하여 해당 게시글의 정보를 조회할 수 있다.

    <img src="README.assets/community-login.png" alt="community" style="zoom:50%;" />
    
    ​			<img src="README.assets/screenshot_1.PNG" alt="community" style="zoom:50%;" />

  ​	<img src="README.assets/screenshot2.PNG" alt="community" style="zoom:50%;" />

  <img src="README.assets/community.PNG" alt="community" style="zoom:50%;" />

  ​									

  <img src="README.assets/newarticle.PNG" alt="newarticle" style="zoom:50%;" />

- ##### 마이페이지

  - 선택한 프로필 사진과 아이디, 닉네임을 볼 수 있고, 회원정보 수정 버튼을 통해 내용을 수정할 수 있다.
  - 별점을 등록한 영화, 찜한 영화, 작성한 게시글, 작성한 한마디를 모아 볼 수 있다.

  <img src="README.assets/mypage.png" alt="mypage" style="zoom:50%;" />

  <img src="README.assets/mypage2.png" alt="mypage" style="zoom:50%;" />

- ##### 회원가입, 로그인 페이지

  - 회원가입 시, 캐릭터 중에서 하나를 골라 프로필 사진으로 사용할 수 있다.
  - 닉네임과 아이디 중복 여부를 검사하여 바로 알려준다.

  <img src="README.assets/signup.PNG" alt="signup" style="zoom:50%;" />

  <img src="README.assets/login.PNG" alt="login" style="zoom:50%;" />

- ##### 회원정보수정 페이지

  - 기존 프로필 정보를 보라색 동그라미로 알려주며, 새로운 사진을 선택함으로써 프로필 사진을 변경할 수 있다.
  - 닉네임은 placeholder로 기존 닉네임이 나와있고, 새로운 닉네임을 입력하여 변경할 수 있다. 단, 기존 닉네임과 겹치면 경고 메시지가 뜬다.
  - 아이디는 수정할 수 없도록 readonly, disabled로 제시된다.
  - 비밀번호와 비밀번호 확인을 입력함으로써 회원 정보 수정을 완료할 수 있다.
  - 회원 정보 수정이 완료되면 마이페이지로 이동된다.

  <img src="README.assets/updateProfile.PNG" alt="updateProfile" style="zoom:50%;" />

## 5. 추천 알고리즘에 대한 설명

👉 영화의 키워드와 장르를 바탕으로, 평점을 고려하여 추천해주는 알고리즘이다.

구체적으로는, TMDB에서 제공하는 관련 영화 API를 활용했다. 왜냐하면, 관련 영화 API 자체가 장르와 키워드를 바탕으로 한 추천 알고리즘을 통과한 결과이기 때문이다. 이에 평점 정보라는 필터를 더하기 위해, 사용자가 평점을 4점 이상 준 영화 각각에 대해 관련 영화를 모은 후, 랜덤 샘플링하여 메인 페이지에 영화 목록을 출력하였다.

평점이 4점 이상인 영화의 관련 영화가 개수를 충족시키지 못하는 경우, 모은 영화들에 관련 영화 데이터를 더하여 랜덤 샘플링했다.

로그인하지 않거나 평점을 남긴 영화가 없어 기반이 되는 평점 데이터가 충족되지 못한 경우, 전체 영화에서 랜덤으로 영화를 추출하여 제공하는 알고리즘을 사용했다.

<u>즉, 평점 데이터가 있는 사용자라면 '평점을 4점 이상으로 준 영화들의 관련영화에서 랜덤 추출', 그게 아니라면 '전체 영화에서 랜덤 추출'의 알고리즘을 구현한 것이다.</u>

> **추천 알고리즘 로직**
>
> 1. 평점 정보를 저장한 movies_rating 테이블에서 request를 보낸 사용자의 rating 정보를 찾아서, 4점 이상인 것들만 추출해 낸다.
>
>    1. 결과로 나온 쿼리셋에서 movie_id를 뽑아서 (즉, 평점을 준 영화의 id), movies_similar 테이블의 original_movie와 일치하는 쿼리셋들을 뽑아낸다.
>
>       즉, 원래 영화의 id가 original_movie로 저장되어 있는 관련영화 테이블에서 movie_id를 매칭하여 관련 영화를 추출해낸다.
>
>    2. 평점을 4점 이상 준 영화가 둘 이상일 수 있으므로, for문을 돌려가며 쿼리셋을 더한다.
>
> 2. 평점을 남긴 영화가 없거나, 평점을 4점 이상 준 영화가 없을 때에는 애초에 필터링으로 완성된 쿼리셋이 존재하지 않는다. 이 경우, 전체 영화를 대상으로 쿼리셋을 구한다.
>
> 3. 구한 쿼리셋을 바탕으로 random 모듈을 통해 carousel에 5개, 영화 목록에 15개를 추출하여 메인 페이지에 제시한다.
>
>    단, carousel에는 영화의 상세정보를 나타내야 하는데 관련 영화에는 상세정보가 존재하지 않는다. 따라서 carousel은 전체 영화를 바탕으로 추천이 진행된다.

```python
# 추천
@api_view(['GET'])
def recommendation(request):
    movie_list = Rating.objects.filter(user=request.user.pk, rate__gte=4)
    result = Similar.objects.none()  # 빈 쿼리셋
    if movie_list:
        for movie in movie_list:
            # movies_similar 테이블에서 original_movie로 필터링 후
            similar_movies = Similar.objects.filter(original_movie=movie.movie_id)
            # 목록에 추가
            result = result | similar_movies   
    else:
        result = Movie.objects.all()
    allmovies = Movie.objects.all()
    random_picked = random.sample(list(result), 15)
    carousel_picked = random.sample(list(allmovies), 5)
    serializer1 = MovieListSerializer(random_picked, many=True)
    serializer2 = MovieSerializer(carousel_picked, many=True)
    return Response({"recommendations": serializer1.data, "carouselItems": serializer2.data})
```

## 6. 느낀 점 (어려웠던 점, 알게 된 점, 재밌었던 점)

- 김민채 (Backend: Django, Vue.js의 JS)

  - DB에 데이터를 넣는 일이 어려웠다. 합의한 목적에 맞는 웹 애플리케이션을 설계하기 위해 필요한 형태의 모델이 있는데, TMDB API에서 주는 정보를 JSON 파일로 받았지만, 결코 내가 의도한 모델의 형태로 주어지지 않기 때문이다. 그리고, API로 JSON 파일을 가져와서 어떻게 DB에 넣을지도 방법을 몰라 어려웠다.

    1. sqlite를 활용해서 INSERT 구문으로 데이터 넣기 🔺

       ⇒ model로 만들어진 테이블을 모두 지우고, CREATE TABLE 등 sql 구문으로 JSON file에 적힌 모양으로 직접 테이블을 만들었다. 그러나, 외래키 관계가 너무 많아서 나중에 데이터를 넣어서 조회를 할 때 외래키 관계가 제대로 작동하지 않았고, 주어진 정보에 맞춰서 model을 변경하다 보니 데이터를 의도대로 사용할 수 없었다.

    2. json 파일을 CSV 파일로 변환한 후 새로운 방법 찾아보기 ❌

    3. json 파일로 fixtures 파일 만들기 ⭕

       ⇒ fixtures를 load하는 방법은 배웠지만 API로 받아온 JSON file의 형태가 fixtures가 요구하는 것과는 달라서 한참을 변환 방법만 찾았다. 이윽고 pjt02에서 데이터를 가공하는 함수를 만들었던 걸 보고, 기존 JSON 파일을 가공해서 fixtures의 형태를 띠도록 만들면 되겠다고 생각하여 실행에 옮겼고, DB에 데이터를 넣을 수 있었다. 특히, API 마다 전해주는 JSON 의 형식이 달라서 fixtures 로 가공하는 함수를 만들어 각각에 적용시키는 방법이 옳았다는 생각을 했다.

  - 키워드로 필터링한 검색결과를 내보낼 때, 필터링할 방법이 생각나지 않아 라이브러리를 알아보았고, 'django-filter' 라이브러리를 사용하려 했다. 그러나 (내가 이해한 한으로는) 공식문서에서 지시하는 기능이 django에서 템플릿을 구현하는 방법이어서 이번 프로젝트에 적절하지 않다고 판단했다. 구글 검색을 하다가 filter 메서드를 기억해냈고, 이를 응용해서 사용했다. 또한, 필터링한 결과물인 쿼리셋을 하나로 합칠 방법을 알지 못했는데 파이프라인으로 합칠 수 있음을 배웠다.

  - 기능을 잘 구현했다고 생각했는데 결과물을 합치고 조정하고 하다보니 오류가 자꾸 발생했다. 잘 작동하던 기능이, 다른 부분을 수정하고 나니 작동하지 않는 경우도 더러 있고, 지속적으로 좋은 품질의 서비스를 제공하기 위해서는 많은 노력이 필요하다는 점을 배웠다.

  - 또한, 코드 정리는 마지막에 할 게 아니라 처음부터 구체적으로 설계하고, 진행하면서 하는 것이 현명하겠다는 생각이 들었다.

  - 그럼에도 하나의 완전한 형태의 사이트를 만들고 유용한 정보를 제공하고 공유할 수 있는 수단을 만든다는 게 신나는 일이었기 때문에 열성을 다해 최종 프로젝트에 임했다.

<br/>

- 윤혜구 (Frontend: Vue.js 전반, 디자인)
  - Vue를 배운지 채 2주가 되지 않은데다가 배운 기간도 2주가량밖에 되지 않아서 프로젝트 시작 전에 뷰를 써야 하나 장고로만 해야 하나 고민을 많이 했다. 결과적으로 이번 프로젝트를 하면서 일주일 전에 비해 훨씬 익숙해졌다고 느껴지기 때문에 도전하길 잘했다는 생각이 든다.
  - 모달 구현이 간단할 줄 알았는데 생각보다 엄청 오래걸렸다. 3일 이상 걸린 것 같다. 처음에는 영화 아이템 컴포넌트 하위에 모달이 있어서 영화 하나마다 모달이 각각, 즉 메인페이지에만 모달이 15개가 있는 구조였는데, 이렇게 하니까 모달이 꺼지지 않도록 backdrop 속성을 주는 게 안먹혀서 한참을 헤맸다. (모달에 있는 찜하기 버튼을 눌러야 하기 때문에 모달을 클릭했을 때 꺼지면 안됐다) 그러다가 부트스트랩 설명 중에 `position:fixed; `를 사용하기 때문에 최대한 상위 태그 안에 넣어야 제대로 동작한다는 문구를 보고 모달을 movieList.vue에 하나만 넣고 데이터만 변경해주는 구조로 변경하였다. 원하는 대로 동작하는 것은 물론이고 구조적으로도 훨씬 깔끔해졌다.
  - 캐러셀과 모달, 버튼 클래스에 부트스트랩을 사용했는데, 간편하다는 건 큰 장점이지만 커스텀이 어렵다는 건 단점이다. 개발자도구를 통해 해당 부트스트랩 컴포넌트가 어떻게 구현되어있나 살펴보고 덮어씌우는 식으로 커스텀했다. 
  - css의 경우에도 처음부터 전체적인 그림을 고려해서 클래스 이름을 잘 짓고 재사용 가능하게 만들면 나만의 라이브러리처럼 페이지별로 일관성 있게 갖다 쓰면서 만들 수 있는데, 그걸 깨달았을 때는 이미 진도가 너무 많이 나가서 고치기 어려워진 바람에 계속 하나하나 스타일을 따로 적용해줬던 점이 아쉽다. (예를 들어 모든 페이지의 전체 중앙 정렬을 다 따로 해줬다) js코드도 마찬가지로 로그인 정보는 모든 페이지에서 참조해야 해야 하니까 vuex에서 관리하는 것이 쉬운데, 처음에 단순히 App.vue도 상위 컴포넌트니까 App에서 관리하자~ 하고 짰다가 많이 뜯어 고쳤다. 일단 생각 없이 더럽게 짰다가 고치면 되지 라고 생각했는데, 한번 잘 되게 연결해놓은 코드에서 사소한거 하나를 슥 고치면 그와 연결된 모든 기능들이 다 틀어져서 에러 지옥이 되기 때문에 생각보다 대대적인 구조 수정은 어렵다는 점을 몸소 체험했다. 나름 처음에 기획을 탄탄히 하고 시작하려고 구체적인 구상을 열심히 하고 시작했는데 페이지 구조와 그에 따른 컴포넌트, 스타일 형식까지 다 처음에 큰 틀정도는 설계를 잘 해줘야 한다는 걸 알게 됐다.  그리고 다음 프로젝트에서는 그 설계를 어떻게 해야겠다는 느낌을 조금 알게 된 것 같다. 
  - 여러가지 에러 해결에 가장 많은 시간을 쏟았다. 마지막까지도 몇 가지 버그와 에러들이 있었는데, 마감 시간이 다가와서 완벽하게 해결하지 못한 점이 아쉬움으로 남는다. 그래도 처음으로 해보는 제대로 된 프로젝트고, 원하는 대로 실제로 동작하는 그럴듯한 사이트를 만들어냈다는 것이 너무 신기하고 재밌다. 프로젝트 기간이 끝나더라도 개인적으로 더 수정해서 깔끔한 서비스를 만들어보고 싶다는 생각이 든다. 

<br>

## 8. 참고한 자료

- [QuerySet API reference](https://www.notion.so/5605d01105a34a65ad5a52003bece8b1#2c31643daf6445979e7f131cde0b0e41)
- [Django Tips # 5 How to Merge QuerySets](https://www.notion.so/5605d01105a34a65ad5a52003bece8b1#315a4ad594bc46fd97a8096e615b7e1e)

- [how to create an empty queryset and to add objects manually in django](https://www.notion.so/5605d01105a34a65ad5a52003bece8b1#360f41a5d72147b2bb6b8db5b4370a20)

- [[Vue.js] ❗TypeError: Cannot read property of undefined](https://www.notion.so/5605d01105a34a65ad5a52003bece8b1#81a820926c534e41aa39b1d1ec8368c2)
- [javaScript) jwt decode하여 payload값 json으로 parsing하는 방법](https://www.notion.so/5605d01105a34a65ad5a52003bece8b1#5b460fd4928742a6a9e49a773c6e7eeb)

* https://getbootstrap.com/docs/5.1/components/modal/
