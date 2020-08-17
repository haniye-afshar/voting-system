from django.db import models 

class Vote(models.Model):
    input1 = models.IntegerField()
    input2 = models.IntegerField()
