"""BookMyMovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import MovieListView, CinemaListView, movie_in_city, movie_in_cinema, seat_available_for_show
from booking.views import book_ticket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieListView.as_view(), name="movie-running"), 
	path('cinema_list/', CinemaListView.as_view(), name="cinema-list"),
	path('movie/city/<str:city_name>', movie_in_city, name="movie-by-city"), #1. all movie playinh in my city
	path('movie/cinema/<int:pk>', CinemaListView.as_view(), name="cinema-list"),
	path('shows/movie/<int:pk>', movie_in_cinema, name="movie-by-cinema"), #2.all cinema in which a movie playing along with showtime
	path('shows/<movie_name>/<cinema_name>', seat_available_for_show, name="seats-for-show"),#3.for each show check seats avalible
	path('book/seats/<int:show_id>', book_ticket, name="book-ticket"),#4.book a ticket
]
