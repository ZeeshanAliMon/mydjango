from django.db import models
from django.utils import timezone
class Login(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length= 100)

    def __str__(self):
        return self.name
class Suggestion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField("Email", max_length=254)
    text = models.TextField("")

    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField("Email", max_length=254)
    text = models.TextField("")

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.name
        

class StudentInfo(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    fname = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    programme = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    cgpa = models.FloatField()

    def __str__(self):
        return self.student.name

class Subject(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subname = models.CharField(max_length= 20)
    mark = models.IntegerField()
    def __str__(self) :
        return self.subname

class RegGpa(models.Model):
    number = models.IntegerField(default = 0)
    time  = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.number} {self.time}"
