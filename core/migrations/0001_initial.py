# Generated by Django 4.1.4 on 2022-12-19 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=200)),
                ('num_of_guests', models.IntegerField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('day_available', models.CharField(max_length=200)),
                ('payment_method', models.PositiveSmallIntegerField(choices=[(1, 'Free'), (2, 'Fixed Price'), (3, 'Any Amount')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_guests', models.IntegerField(max_length=200)),
                ('first_day', models.CharField(max_length=200)),
                ('last_day', models.CharField(max_length=80)),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.accommodation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]