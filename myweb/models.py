from django.db import models
from django.contrib.auth.models import User


class Travel(models.Model):
    travel_name = models.CharField(max_length=200,blank=True)
    travel_wherename = models.CharField(max_length=200,blank=True)
    travel_detail = models.CharField(max_length=500,blank=True)
    travelimg = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return f'{self.travel_name} , {self.travel_wherename} , {self.travel_detail}'


class TravelType(models.Model):
    type_travel = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return f'{self.type_travel}'

class TravelPlaceKeeper(models.Model):
    travel_name = models.ForeignKey(Travel, on_delete=models.CASCADE)
    Keeper_travel_name = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f'ผู้ดูแลสถานที่ : {self.Keeper_travel_name}'

#models.ForeignKey(TravelType, on_delete=models.CASCADE)