from rest_framework import serializers

from .models import Booking, Seat

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = "__all__"

class SeatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Seat
		fields = "__all__"

