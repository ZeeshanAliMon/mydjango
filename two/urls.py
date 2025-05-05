from django.contrib import admin
from django.urls import path
from two  import views
urlpatterns = [
    path('', views.home,name="home"),
    path('home', views.home,name="home"),
    path('about', views.about,name="about"),
    path('contactUs', views.contactUs,name="contactUs"),
    path('login/', views.login,name="login"),
    path('about', views.about,name="about"),
    
    path('suggestion', views.suggestion,name="suggestion"),
    path('gpaCalculator', views.gpaCalculator,name="gpaCalculator"),
    path('page_not_available', views.PageNotAvailable,name="page_not_available"),
    path('jaal', views.jaal,name="jaal"),
    path('templogin', views.templogin,name="templogin"),
    path('student', views.student,name="student"),
    path('studentinfo/<int:roll>', views.studentinfo,name="studentinfo"),
    path('commit', views.commit,name="commit"),
    path('result', views.result,name="result"),
    path('commitresult', views.commitresult,name="commitresult"),
    path('chromeex', views.chromeex,name="chromeex"),

   
    
 
]
