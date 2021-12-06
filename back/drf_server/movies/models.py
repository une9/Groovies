from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import CharField


class Movie(models.Model):
    adult = models.BooleanField()
    genres = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=150)
    tagline = models.CharField(max_length=100, blank=True)
    overview = models.TextField(null=True)
    runtime = models.PositiveIntegerField(blank=True, null=True)
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200, blank=True)
    trailer_key = models.CharField(max_length=100, blank=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    like_comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comment")


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)
    character = models.CharField(max_length=50, blank=True)
    movie_id = models.ForeignKey(Movie, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)
    movie_id = models.ForeignKey(Movie, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Similar(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200, blank=True)
    adult = models.BooleanField()
    original_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)