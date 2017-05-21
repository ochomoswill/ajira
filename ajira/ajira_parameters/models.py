from django.db import models
from django.utils import timezone

# Create your models here.


class Countries(models.Model):
    country_abbr = models.CharField(max_length=10)
    country_code = models.IntegerField()
    country_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.country_name


class Counties(models.Model):
    county_code = models.IntegerField()
    county_name = models.CharField(max_length=50)
    country_id = models.ForeignKey(Countries,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.county_name

class Constituencies(models.Model):
    constituency_name = models.CharField(max_length=50)
    county_id = models.ForeignKey(Counties,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.constituency_name

