from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *
from app1.forms import *

def insertIntoFormsDepartment(request):
    d=DepartmentForm()
    v={'DADDY':d} #send this to html file
    if request.method=='POST':
        dd=DepartmentForm(request.POST)
        if dd.is_valid():
            ddd=dd.cleaned_data['sub']
            dde=dd.cleaned_data['fee']
            Tq=Department.objects.get_or_create(sub=ddd,fee=dde)[0]
            Tq.save()
            return HttpResponse(str(dd.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render (request,'insertIntoFormsDepartment.html',v)

def insertIntoFormstudent(request):
    d=StudentForm()
    v={'DADDY':d} #send this to html file
    if request.method=='POST':
        dd=StudentForm(request.POST)
        if dd.is_valid():
            a=dd.cleaned_data['sub']
            b=dd.cleaned_data['sname']
            c=dd.cleaned_data['num']
            d=dd.cleaned_data['paid']
            e=dd.cleaned_data['username']
            f=dd.cleaned_data['password']
            Tq=Student.objects.get_or_create(sub=a,sname=b,num=c,paid=d,username=e,password=f)[0]
            Tq.save()
            return HttpResponse(str(dd.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render (request,'insertIntoFormsStudent.html',v)

def insertIntoFormDeclaration(request):
    d=DeclarationForm()
    v={'DADDY':d} #send this to html file
    if request.method=='POST':
        dd=DeclarationForm(request.POST)
        if dd.is_valid():
            b=dd.cleaned_data['sname']
            c=dd.cleaned_data['code']
            d=dd.cleaned_data['verify']
            Tq=Declaration.objects.get_or_create(sname=b,code=c,verify=d)[0]
            Tq.save()
            return HttpResponse(str(dd.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render (request,'insertIntoFormsDeclaration.html',v)
