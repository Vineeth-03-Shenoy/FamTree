from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Family_Member

class NewMemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["FamMemberID"].widget.attrs.update({
            'required':'',
            'name':'FamMemberID',
            'id':'FamMemberID',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter FamMemberID',
            'maxlength':'18',
            'minlength':'18'
        })
        self.fields["Fname"].widget.attrs.update({
            'required':'',
            'name':'Fname',
            'id':'Fname',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter First Name',
            'maxlength':'30',
            'minlength':'2'
        })
        self.fields["Name"].widget.attrs.update({
            'required':'',
            'name':'Name',
            'id':'Name',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter Name',
            'maxlength':'30',
            'minlength':'2'
        })
        self.fields["Lname"].widget.attrs.update({
            'required':'',
            'name':'Lname',
            'id':'Lname',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter Last Name',
            'maxlength':'30',
            'minlength':'2'
        })
        self.fields["DoB"].widget.attrs.update({
            'required':'',
            'name':'DoB',
            'id':'DoB',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter Date of Birth (YYYY-MM-DD)',
            'maxlength':'10',
            'minlength':'10'
        })
        self.fields["Gender"].widget.attrs.update({
            'required':'',
            'name':'Gender',
            'id':'Gender',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter Gender (M-male, F-female)',
            'maxlength':'1',
            'minlength':'1'
        })


    FamMemberID = forms.CharField(label='Enter ID', min_length=18, max_length=18)
    Fname = forms.CharField(label='Enter Fname', min_length=2, max_length=30)
    Name = forms.CharField(label='Enter Name', min_length=2, max_length=30)
    Lname = forms.CharField(label='Enter Lname', min_length=2, max_length=30)
    DoB = forms.DateField(label='Enter DoB')
    Gender = forms.CharField(label='Enter Gender', min_length=1, max_length=1)

    def clean_FamMemberID(self):
        FamMemberID = self.cleaned_data['FamMemberID']
        r = Family_Member.objects.filter(FamMemberID=FamMemberID)
        if r.count():
            raise  ValidationError("ID already exists")
        return FamMemberID

    def clean_Fname(self):
        Fname = self.cleaned_data['Fname']
        return Fname

    def clean_Name(self):
        Name = self.cleaned_data['Name']
        return Name

    def clean_Lname(self):
        Lname = self.cleaned_data['Lname']
        return Lname
    
    def clean_DoB(self):
        DoB = self.cleaned_data['DoB']
        return DoB

    def clean_Gender(self):
        Gender = self.cleaned_data['Gender']
        return Gender

    def save(self, commit=True):
        user = Family_Member.objects.create_user(
            self.cleaned_data['FamMemberID'],
            self.cleaned_data['Fname'],
            self.cleaned_data['Name'],
            self.cleaned_data['Lname'],
            self.cleaned_data['DoB'],
            self.cleaned_data['Gender']
        )
        return user

    class Meta:
        model = Family_Member
        fields = ['FamMemberID','Fname','Name','Lname','DoB','Gender',]


class DeleteMemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["FamMemberID"].widget.attrs.update({
            'required':'',
            'name':'FamMemberID',
            'id':'FamMemberID',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter FamMemberID',
            'maxlength':'18',
            'minlength':'18'
        })

    class Meta:
        model = Family_Member
        fields = ['FamMemberID',]


class SearchMemberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["FamMemberID"].widget.attrs.update({
            'required':'',
            'name':'FamMemberID',
            'id':'FamMemberID',
            'type':'text',
            'class':'form-input',
            'placeholder':'Enter FamMemberID',
            'maxlength':'18',
            'minlength':'18'
        })

    class Meta:
        model = Family_Member
        fields = ['FamMemberID',]