from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from movies.models import Cart, Movie, Rating, Comment
from community.models import Article
from movies.serializers import MovieListSerializer, CommentSerializer
from community.serializers import ArticleListSerializer
from django.contrib.auth import get_user_model


@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    #1-3. 닉네임 중복 여부 체크
    nickname = request.data.get('nickname')
    if get_user_model().objects.all().filter(nickname=nickname).exists():
        return Response({'error': '이미 사용중인 닉네임입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    #1-4. 유저네임 중복 여부 체크
    username = request.data.get('username')
    if get_user_model().objects.all().filter(username=username).exists():
        return Response({'error': '이미 사용중인 아이디입니다.'}, status=status.HTTP_400_BAD_REQUEST)

	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password')) # 암호화
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 회원정보 수정
@api_view(['PUT'])
def update(request, profile_pk):
    #0. 기존 사용자 정보
    user_info = get_user_model().objects.get(pk=profile_pk)
    #1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    #1-3. 닉네임 중복 여부 체크
    nickname = request.data.get('nickname')
    if nickname != user_info.nickname:
        if get_user_model().objects.filter(nickname=nickname).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data, instance=user_info)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password')) # 암호화
        user.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request, profile_pk):
    user = get_user_model().objects.get(pk=profile_pk)
    user.delete()
    return Response({'message': '회원 탈퇴가 완료되었습니다. 안녕히 가십시오.'}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def show_cart(request):
    cart_list = Cart.objects.filter(user=request.user)
    if cart_list:
        movies = Movie.objects.none()
        for item in cart_list:
            movie = Movie.objects.filter(pk=item.movie.id)
            movies = movies | movie
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def rated_movies(request):
    rated_list = Rating.objects.filter(user=request.user)
    if rated_list:
        movies = Movie.objects.none()
        for item in rated_list:
            movie = Movie.objects.filter(pk=item.movie.id)
            movies = movies | movie
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)
    return Response({'message': '영화에 첫 평점을 남겨주세요!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def my_comments(request):
    comment_list = Comment.objects.filter(user=request.user)
    if comment_list:
        serializers = CommentSerializer(comment_list, many=True)
        return Response(serializers.data)
    return Response({'message': '영화에 첫 한마디를 남겨주세요!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def my_articles(request):
    article_list = Article.objects.filter(user=request.user)
    if article_list:
        serializers = ArticleListSerializer(article_list, many=True)
        return Response(serializers.data)
    return Response({'message': '커뮤니티에 첫 게시글을 남겨주세요!'})



# 전체 유저정보 조회
@api_view(['GET'])
def all_profile(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# 개별 프로필 조회
@api_view(['GET'])
def profile(request, profile_pk):
    user = get_user_model().objects.get(pk=profile_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)