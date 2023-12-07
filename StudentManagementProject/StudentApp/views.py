from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from StudentApp.models import Course, City, Student


# Create your views here.
def login_fun(request):
    if request.method=="POST":
        user_name=request.POST['txtUserName']
        user_pswd=request.POST['txtPassword']
        u1=authenticate(username=user_name,password=user_pswd) # it will return user object
        if u1 is not None:
            if u1.is_superuser: # checking whether the data is superuser or not
                request.session['Uname']=user_name # it will used whatever the page we need to use
                return redirect('home')
        else:
            return render(request,'login.html',{'msg':'username and password is incorrect'})
    else:
        return render(request,'login.html')

def register_fun(request):
    if request.method=="POST":#this code will execute when we click on submit button in register.html page
        user_name=request.POST['txtUserName']
        user_pswd=request.POST['txtPassword']
        user_email=request.POST['txtMail']
        u1=User.objects.create_superuser(username=user_name,password=user_pswd,email=user_email)
        u1.save()
        return redirect('log')

    else:# this code will execute when we click on the hyperlink in login html page
        return render(request,'register.html')


def home_fun(request):
    return render(request,'home.html',{'data':request.session['Uname']})


def addcourse_fun(request):
    if request.method=='POST':
        c1=Course()
        c1.course_name=request.POST['txtCourseName']
        c1.course_duration=request.POST['txtCourseDuration']
        c1.course_fees=int(request.POST['txtCourseFee'])
        c1.save()
        return render(request,'addcourse.html',{'msg':'sucessfully added'})
    else:
        return render(request,'addcourse.html')


def display_course_fun(request):
    course_data=Course.objects.all() # it will return list of objects
    return render(request,'displaycourse.html',{'data':course_data})


def update_course_fun(request,courseid):
    c1=Course.objects.get(id=courseid)
    if request.method=='POST':
        c1.course_name=request.POST['txtCourseName']
        c1.course_duration=request.POST['txtCourseDuration']
        c1.course_fees=int(request.POST['txtCourseFee'])
        c1.save()
        return redirect('display_course')
    else:
        return render(request,'updatecourse.html',{'data':c1})


def deletecourse_fun(request,courseid):
    c1=Course.objects.get(id=courseid)
    c1.delete()
    return redirect('display_course')


def addstudent_fun(request):
    if request.method=='POST':
        s1=Student()
        s1.stud_name=request.POST['txtName']
        s1.stud_phno=request.POST['txtPhno']
        s1.stud_email=request.POST['txtmail']
        s1.stud_city=City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course=Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.paid_fees=int(request.POST['txtpaidfee'])
        c1=Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.pending_fees=c1.course_fees - s1.paid_fees
        s1.save()
        return redirect('addstudent')

    else:
        city=City.objects.all()
        course=Course.objects.all()
        return render(request,'addstudent.html',{'Citydata':city,'Coursedata':course})


def displaystudent_fun(request):
    s1=Student.objects.all()
    return render(request,'displaystudent.html',{'studentdata':s1})


def updatestudent_fun(request,stud_id):
    s1=Student.objects.get(id=stud_id)
    if request.method=='POST':
        s1.stud_name = request.POST['txtName']
        s1.stud_phno = request.POST['txtPhno']
        s1.stud_email = request.POST['txtmail']
        s1.stud_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.stud_course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.paid_fees = s1.paid_fees + int(request.POST['txtpaidfee'])
        c1 = Course.objects.get(course_name=request.POST['ddlcourse'])
        if s1.pending_fees>0:
            s1.pending_fees = c1.course_fees - s1.paid_fees
        else:
            s1.pending_fees=0
        s1.save()
        return redirect('displaystudent')
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request,'updatestudent.html',{'student':s1,'Citydata':city,'Coursedata':course})


def deletestudent_fun(request,stud_id):
    s1 = Student.objects.get(id=stud_id)
    s1.delete()

    return redirect('displaystudent')