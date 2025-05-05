from django.contrib import admin
from django.urls import path
from cropPredictor  import views
urlpatterns = [
    path('', views.predict_crop,name="cropPredictor"),
   
 
]
