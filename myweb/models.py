from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'




class TravelType(models.Model):
    travel_name = models.CharField(max_length=200)
    travel_wherename = models.CharField(max_length=200)
    travel_detail = models.TextField(null=100)

    def __str__(self):
        return f'{self.travel_name}'


class Travel(models.Model):
    type_travel = models.CharField(max_length=200)

def __str__(self):
        return f'{self.type_trave}'

class Traveluser(models.Model):
    travel_text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

#models.ForeignKey(TravelType, on_delete=models.CASCADE)