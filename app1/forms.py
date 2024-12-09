from typing import Any
from django import forms
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator #builtin validators mr.dev.vk
from app1.models import *
from app1.views import *

def validator1(value): 
    if value[0]=='v': #indexing #The subject does not  start with letter 'v' 
        return forms.ValidationError('should not starts with v')
def validator2(value):
    if len(value)<2:
        raise forms.ValidationError('length should  be more than 2')
class DepartmentForm(forms.Form):
    sub=forms.CharField(validators=[validator1,validator2])
    fee=forms.CharField(validators=[RegexValidator('[6-8]\d{7}')])# built-in validators


class StudentForm(forms.Form):
    sub=forms.ModelChoiceField(queryset=Department.objects.all(), required=True)
    sname=forms.CharField()
    num=forms.CharField(min_length=10,max_length=10,validators=[RegexValidator('[6-9]\d{9}')]) 
    paid=forms.IntegerField()
    username=forms.CharField(validators=[RegexValidator('^[a-zA-Z0-9]{5,10}$')])
    password=forms.CharField(validators=[RegexValidator('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')])
    
    # FORM CLASS OBJECT METHODS
    re_enter_password=forms.CharField(validators=[RegexValidator('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')])
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False) #BOT PERPOSE KINGUUUU

    def check(self):
        password=self.cleaned_data['password']
        re_enter_password=self.cleaned_data['re_enter_password']
        if password!=re_enter_password:
            raise forms.ValidationError('chech the password')

class DeclarationForm(forms.Form):
    sname=forms.ModelChoiceField(queryset=Student.objects.all(), required=True)
    code=forms.CharField()
    verify=forms.CharField()