from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.login_fun,name='log'),# it will redirect to login.html page
    path('reg',views.register_fun,name='reg') ,# it will redirect to register htmlpage and create account
    path('home',views.home_fun,name='home'),#it will redirect to home html page
    path('add_course',views.addcourse_fun,name='add_course'), #redirecting to addcourse html page and inserting course data into course table
    path('display_course',views.display_course_fun,name='display_course'), #it will collect all data from course table  and send to dispay_course html pace
    path('update_course/<int:courseid>',views.update_course_fun,name='update_course'),
    path('delete_course/<int:courseid>',views.deletecourse_fun,name='delete_course'),# it will delete the course data from the course table
    path('addstudent',views.addstudent_fun,name='addstudent'), # it will display addstudent.html file and after read the data from file and store it in student html
    path('displaystudent',views.displaystudent_fun,name='displaystudent'),
    path('updatestudent/<int:stud_id>',views.updatestudent_fun,name='updatestudent'),
    path('deletestudent/<int:stud_id>',views.deletestudent_fun, name='deletestudent')
]

