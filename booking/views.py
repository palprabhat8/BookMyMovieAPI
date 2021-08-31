from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, JsonResponse
from django.db.models import Subquery
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializers import BookingSerializer, SeatSerializer
from dashboard.models import Show
from .models import Booking, Seat


@api_view(['POST'])
@login_required
def book_ticket(request, show_id):
	show = Shows.objects.filter(id=show_id).first()
	if show.available_seats > 0:
		serializer = BookingSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			show.available_seats -=1
			return Response(serializer.data)
		return Response(serializer.errors)


@csrf_exempt
@require_http_methods(['POST'])
def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            return JsonResponse({'status': True, 'message': 'Login Successful'})
        else:
            return JsonResponse({'status': False, 'message': 'Account is disabled'})

@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({'status': 'disconnected', 'message': 'You have been logged out successfully'})


@csrf_exempt
def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        print(username, password, email)
        user = User.objects.create_user(username, email, password)
        user.save()
        return JsonResponse({"status": "Registration Successful"}, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({"status": "Only POST method is allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

