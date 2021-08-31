from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Movie(models.Model):
	lang_choice = (
        ('ENGLISH', 'English'),
        ('BENGALI', 'Bengali'),
        ('HINDI', 'Hindi'),
        ('TAMIL', 'Tamil'),
        ('TELUGU', 'Telugu'))
	name = models.CharField(max_length=20, null=True, blank=True)
	director = models.CharField(max_length=20, null=True, blank=True)
	language = models.CharField(max_length=10, choices=lang_choice)
	run_length = models.IntegerField(help_text="Enter run length in minutes",null=True,blank=True)

	def __str__(self):
		return self.name


class Cinema(models.Model):
	city_choice=(
        ('DELHI','Delhi'),
        ('KOLKATA','Kolkata'),
        ('MUMBAI','Mumbai'),
        ('CHENNAI','Chennai'),
        ('BANGALORE','Bangalore'),
        ('HYDERABAD','Hyderabad'))
	name = models.CharField(max_length=50,null=False, default="Waves Cinema")
	city = models.CharField(max_length=20,choices=city_choice,null=False)
	address = models.CharField(max_length=60)

	def __str__(self):
		return self.name+"-"+self.address+"-"+self.city



class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    total_seats = models.IntegerField(default=20)
    available_seats = models.IntegerField(default=20)

    def __str__(self):
        return str(self.movie) + "-" + str(self.cinema) + "-" + str(self.date) + "-" + str(self.start_time)



