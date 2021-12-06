from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('mycart/', views.show_cart, name='show_cart'), # 찜한 영화 목록 반환
    path('myrated/', views.rated_movies, name='rated_movies'),    # 평점 남긴 영화의 목록 반환
    path('mycomments/', views.my_comments, name='my_comments'),   # 작성한 한줄 댓글 목록 반환
    path('myarticles/', views.my_articles, name='my_articles'),     # 작성한 게시글 목록 반환
    path('api-token-auth/', obtain_jwt_token),
    path('profile/', views.all_profile, name='all_profile'),    # 전체 유저정보 조회
    path('profile/<int:profile_pk>/', views.profile, name='profile'),   # 개별 프로필 조회
    path('profile/<int:profile_pk>/update/', views.update, name='update'),   # 회원정보 수정
    path('profile/<int:profile_pk>/delete/', views.delete, name='delete'),  # 회원탈퇴
]