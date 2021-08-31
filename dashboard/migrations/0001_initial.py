# Generated by Django 3.2.6 on 2021-08-30 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Waves Cinema', max_length=50)),
                ('city', models.CharField(choices=[('DELHI', 'Delhi'), ('KOLKATA', 'Kolkata'), ('MUMBAI', 'Mumbai'), ('CHENNAI', 'Chennai'), ('BANGALORE', 'Bangalore'), ('HYDERABAD', 'Hyderabad')], max_length=20)),
                ('address', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('director', models.CharField(blank=True, max_length=20, null=True)),
                ('language', models.CharField(choices=[('ENGLISH', 'English'), ('BENGALI', 'Bengali'), ('HINDI', 'Hindi'), ('TAMIL', 'Tamil'), ('TELUGU', 'Telugu')], max_length=10)),
                ('run_length', models.IntegerField(blank=True, help_text='Enter run length in minutes', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('total_seats', models.IntegerField(default=20)),
                ('available_seats', models.IntegerField(default=20)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.movie')),
            ],
        ),
    ]
