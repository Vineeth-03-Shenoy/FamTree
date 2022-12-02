from django.db import models

# Create your models here.
class Family_Member(models.Model):
    member_ID=models.CharField(max_length=20)
    FName=models.CharField(max_length=20)
    Name=models.CharField(max_length=25)
    LName=models.CharField(max_length=20)
    DoB=models.DateField()
    registered=models.DateTimeField(auto_now=True)
    DoD=models.DateField()