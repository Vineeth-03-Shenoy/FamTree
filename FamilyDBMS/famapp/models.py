from django.db import models

# Create your models here.
class Family_Member(models.Model):
    FamMemberID = models.CharField(max_length=20, primary_key=True)
    Fname = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    DoB = models.DateField()
    DoD = models.DateField()
    Gender = models.CharField(max_length=2)

class Couple_Family(models.Model):
    Couple_ID = models.CharField(max_length=20, primary_key=True)
    Hus = models.OneToOneField(Family_Member, on_delete=models.CASCADE)
    Wife = models.CharField(max_length=20)
    Wed_ann = models.DateField()

class Parents(models.Model):
    child_ID = models.OneToOneField(Family_Member, on_delete=models.CASCADE, primary_key=True)
    parents_ID = models.ManyToManyField(Couple_Family)

class Personal_Info(models.Model):
    member_ID = models.OneToOneField(Family_Member,on_delete=models.CASCADE,primary_key=True)
    Ph_prefix = models.IntegerField()
    Phone = models.BigIntegerField()
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Email = models.EmailField()
    Job_or_student = models.CharField(max_length=50)
    Company_or_School = models.CharField(max_length=50)
    privilege = models.BooleanField()

class Families(models.Model):
    Family_ID = models.CharField(max_length=20, primary_key=True)
    Fam_Name = models.CharField(max_length=50)
    Members = models.IntegerField()

class Events(models.Model):
    Event_ID = models.CharField(max_length=30, primary_key=True)
    Event_Name = models.CharField(max_length=100)
    Venue = models.CharField(max_length=100)
    Date = models.DateField()

class Invitees(models.Model):
    Event_code = models.ManyToManyField(Events)
    Family_invited = models.ManyToManyField(Families)
    Couple_invited = models.ManyToManyField(Couple_Family)

