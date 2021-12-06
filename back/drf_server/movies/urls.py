from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),   # 영화 상세정보
    path('<int:movie_pk>/actor/', views.movie_actor, name='movie_actor'),   # 배우
    path('<int:movie_pk>/director/', views.movie_director, name='movie_director'),   # 감독
    path('<int:movie_pk>/similar/', views.movie_similar, name='movie_similar'),   # 관련영화
    path('<int:movie_pk>/comment/', views.comment_list),
    path('<int:movie_pk>/comment/create/', views.comment_create),
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_pk>/comment/<int:comment_pk>/like/', views.comment_like),    
    path('<int:movie_pk>/rating/', views.rating),   # user의 rating
    path('<int:movie_pk>/cart/', views.add_cart, name='add_cart'),  # 찜하기
    path('search/<str:keyword>/', views.search, name='search'), # 검색 결과 반환
    path('recommendation/', views.recommendation, name='recommendation'),   # 추천영화 목록 반환
]
