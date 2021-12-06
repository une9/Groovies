from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    path('<int:article_pk>/like/', views.article_like, name='article_like'),
    path('<int:article_pk>/comment/', views.comment_list, name='comment_list'),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('<int:article_pk>/comment/create/', views.comment_create, name='comment_create'),
]