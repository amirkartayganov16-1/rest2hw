from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import *


@api_view (['GET'])
def director_list_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializers(director, many=True)
    return Response(data=serializer.data)


@api_view (['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'Error':'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorCountSerializer(director).data
    return Response(data=data)



@api_view (['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(data=serializer.data)



@api_view (['GET'])
def movie_detail_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'Error':'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializers(movies).data
    return Response(data=data)



@api_view (['GET'])
def review_list_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializers(review, many=True)
    return Response(data=serializer.data)


@api_view (['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Error':'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializers(review).data
    return Response(data=data)

@api_view(['GET'])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializers(movie_reviews, many=True).data
    return Response(data=data)