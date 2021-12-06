from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from community.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


# 게시글 전체 조회, 게시글 작성
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    if articles:
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    return Response(None)


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글 detail           
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 게시글 좋아요
@api_view(['GET', 'POST'])
def article_like(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        if article.like_article_users.filter(pk=request.user.pk).exists():
            liked = True
        else:
            liked = False
        like_status = {
            'liked': liked, # 좋아요 여부
            'count': article.like_article_users.count(),
        }
        return Response(like_status, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if article.like_article_users.filter(pk=request.user.pk).exists():
            article.like_article_users.remove(request.user)
        else:
            article.like_article_users.add(request.user)
        return Response(status=status.HTTP_200_OK)
    

# 전체 댓글      
@api_view(['GET'])
def comment_list(request, article_pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(article=article_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# 댓글 조회, 수정, 삭제    
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk, article_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, article=article_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        if comment.user != request.user:
            return Response({'error': '권한이 없습니다.'})
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        elif request.method == 'DELETE':
            comment.delete()
            data = {
                'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

# 댓글 생성    
@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
