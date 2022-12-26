from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Family_Member


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