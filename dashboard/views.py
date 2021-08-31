from django.shortcuts import render

# Create your views here.
from django.db.models import Subquery
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from .serializers import MovieSerializer, CinemaSerializer, ShowSerializer
from .models import Cinema, Movie, Show

class MovieListView(mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = MovieSerializer
	queryset = Movie.objects.all()
	def get(self, request, *args, **kwargs):
		return self.list(self, request, *args, **kwargs)

class CinemaListView(mixins.ListModelMixin, generics.GenericAPIView):
	serializer_class = CinemaSerializer
	queryset = Cinema.objects.all()

	def get(self, request, *args, **kwargs):
		return self.list(self, request, *args, **kwargs)


@api_view(['GET'])
def movie_in_city(request, city_name):
	cinema = Cinema.objects.filter(city="Mumbai").first()
	print(cinema)
	print(cinema.values('id'))
	movies= Show.objects.filter(cinema__in=Subquery(cinema.values('id')))
	# movies = Show.objects.select_related('movie')
	# print(movies)
	# print("-------------------")
	serializer = ShowSerializer(movies, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def movie_in_cinema(request, movie_name):
	movie_id = Show.objects.filter(name=movie_name)
	shows_cinema = Show.objects.filter(movie__in=Subquery(movie_id.value('id')))
	cinemsa = Cinema.object.filter(id__in=Subquery(shows_cinema.value('id')))
	print(shows_cinema)
	# print("-------------------")
	serializer = ShowSerializer(shows_cinema, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def seat_available_for_show(request, movie_name, cinema_name):
	movie = Movie.objects.filter(name=movie_name).first()
	cinema = Cinema.objects.filter(name = cinema_name).first()
	queryset = Show.objects.filter(movie=movie.id, cinema=cinema.id)
	serializer = ShowSerializer(queryset)
	return Response(serializer.data)
