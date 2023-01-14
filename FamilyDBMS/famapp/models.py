from django.db import models

# Create your models here.
class Family_Member(models.Model):
    FamMemberID = models.CharField(max_length=20, primary_key=True)
    Fname = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    DoB = models.DateField()
    DoD = models.DateField(null=True)
    Gender = models.CharField(max_length=2)
    registered_on = models.DateTimeField(auto_now_add=True)

class Couple_Family(models.Model):
    Couple_ID = models.CharField(max_length=20, primary_key=True)
    Hus = models.ForeignKey(Family_Member, on_delete=models.CASCADE, related_name='husband', to_field='FamMemberID')
    Wife = models.ForeignKey(Family_Member, on_delete=models.CASCADE, related_name='wife', to_field='FamMemberID')
    Wed_ann = models.DateField()

class Parents(models.Model):
    id = models.AutoField(primary_key=True)
    child_ID = models.ForeignKey(Family_Member, on_delete=models.CASCADE, related_name='child', to_field='FamMemberID')
    parents_ID = models.ForeignKey(Couple_Family, on_delete=models.CASCADE, related_name='parent', to_field='Couple_ID')

class Personal_Info(models.Model):
    member_ID = models.OneToOneField(Family_Member,on_delete=models.CASCADE,primary_key=True)
    Ph_prefix = models.CharField(max_length=6)
    Phone = models.CharField(max_length=18)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Pincode=models.CharField(max_length=15, null=True)
    Email = models.EmailField()
    Job_or_student = models.CharField(max_length=50)
    Company_or_School = models.CharField(max_length=50)

class Families(models.Model):
    Family_ID = models.CharField(max_length=20, primary_key=True)
    Fam_Name = models.CharField(max_length=50)
    Members = models.IntegerField()

class Events(models.Model):
    Event_ID = models.AutoField(primary_key=True)
    Event_Name = models.CharField(max_length=100)
    Venue = models.CharField(max_length=100)
    Date = models.DateField()

class MemberInvited(models.Model):
    Event_code = models.ForeignKey(Events, on_delete=models.CASCADE, to_field='Event_ID')
    Member_Invited = models.ForeignKey(Family_Member, on_delete=models.SET_NULL, null=True, to_field='FamMemberID')

class FamilyInvited(models.Model):
    Event_code = models.ForeignKey(Events, on_delete=models.CASCADE, to_field='Event_ID')
    Family_invited = models.ForeignKey(Families, on_delete=models.SET_NULL, null=True, to_field='Family_ID')

class CoupleInvited(models.Model):
    Event_code = models.ForeignKey(Events, on_delete=models.CASCADE, to_field='Event_ID')
    Couple_invited = models.ForeignKey(Couple_Family, on_delete=models.SET_NULL, null=True, to_field='Couple_ID')
