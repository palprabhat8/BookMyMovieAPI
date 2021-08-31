from django.db import models
from django.contrib.auth import get_user_model
from dashboard.models import Show

# Create your models here.
User = get_user_model()

class Booking(models.Model):
    payment_choice = (
        ('Credit Card', 'Credit Card'),
    )
    booking_id = models.CharField(primary_key=True, max_length=200)
    timestamp = models.DateTimeField(
        '%Y-%m-%d %H:%M:%S', null=True, blank=True)
    payment_type = models.CharField(
        max_length=11, choices=payment_choice, default='Credit Card')
    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    paid_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return str(self.booking_id)

class Seat(models.Model):
    seat_number = models.CharField(max_length=3,null=True,blank=False)
    is_booked = models.BooleanField(default=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True, null=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat_number', 'show')

    def __str__(self):
        return self.seat_number + str(self.show)
