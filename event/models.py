from django.db import models

# Create your models here.
    
class EventRegist(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    eventname=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.email

class GrupRegist(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    teamname=models.CharField(max_length=50)
    eventname=models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return self.email

