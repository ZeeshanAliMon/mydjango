from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
import pandas as pd

from .forms import StudentForm
from two.models import Login,Suggestion,ContactUs,Student,StudentInfo,Subject,RegGpa

import time
def home(request):
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contactUs(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("text")
        contactus = ContactUs(name=name,email=email,text=text)
        contactus.save()
        messages.success(request, "Message has been Sent Successfully.")
        return redirect("home")
    return render(request,'contactUs.html')

def PageNotAvailable(request):
    return render(request, 'page_not_available.html')
def login(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        login = Login(name=name,password=password)
        login.save()
        messages.success(request, "Now this name and password is saved in our database.")
       
        return redirect('home')
       

    return render(request, 'login.html')

def suggestion(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("text")

        suggestion = Suggestion(name=name,email=email,text=text)
        messages.success(request, "Thank You . Your name, Email and Suggestion is saved in our database.")
        suggestion.save()
        
        return redirect('home')
    return render(request,'suggestion.html')

def gpaCalculator(request):
    try:
        last_reg_gpa = RegGpa.objects.order_by('-number').first()
        last_number = last_reg_gpa.number if last_reg_gpa else 0
    except RegGpa.DoesNotExist:
        last_number = 0
    last_number +=1
    number = RegGpa(number = last_number)
    number.save()
    return render(request,"gpaCalculator.html")

def jaal(request):
    return render(request,"jaal.html")
def templogin(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        login = Login(name=name,password=password)
        login.save()
        messages.success(request, "Now this name and password is saved in our database.")
       
        return redirect('home')
       

    return render(request, 'templogin.html')



def student(request,roll=0):
    # if roll !=0:
        # students= Student.objects.all()
        # # student = Student.objects.get(roll=roll)
        # # studentinfo = StudentInfo.objects.get(student=student)
        # # context = {"Studentinfo": studentinfo,"Students":students}
        # context = {"studentinfo": roll,"Students":students}
        # return render(request,"student.html",context=context)
   

    students = Student.objects.all()

    context = {"students": students}
    for student in students:
        print(student.name)
    return render(request, 'student.html', context)
def studentinfo(request, roll):
    students = Student.objects.all()
    student = Student.objects.get(roll=roll)
    studentinfo = StudentInfo.objects.get(student=student)
    context= {"students":students,"studentinfo":studentinfo}
    return render(request, 'student.html', context)
def commit(request):
    Student.objects.all().delete()
    StudentInfo.objects.all().delete()

    file = "./student.xlsx"
    try:
        df = pd.read_excel(file)
        print("File found")
    except FileNotFoundError:
        print("File not found")
        df = pd.DataFrame(columns=['Name', 'Roll No', 'Father Name', 'Department', 'Programme', 'Contact', 'CGPA'])

    for index, row in df.iterrows():
        name = row["Name"]
        roll = int(row["Roll No"]) 
        student = Student(name=name, roll=roll)
        student.save()

        fname = row["Father Name"]
        department = row["Department"]
        programme = row["Programme"]
        contact = row["Contact"]
        cgpa = row["CGPA"]

        student_info = StudentInfo(student=student, fname=fname, department=department, programme=programme,contact=contact, cgpa=cgpa)
        student_info.save()

    return HttpResponse("Committed")
def commitresult(request):
    rolls = [1,2,3,92,93,94,22144]
    Subject.objects.all().delete()
    for roll in rolls:
        student = Student.objects.get(roll=roll)
        try:
            Subject.objects.filter(student = student).delete()
        except :
            pass
        
        file = 'result.xlsx'
        df = pd.read_excel(file)
        for index , row in df.iterrows():
            subject = Subject(student=student,subname=row["Subject"],mark=row[roll])
            subject.save()
    return HttpResponse("result commited")
def result(request):
    if request.method == "POST":
        
        roll = request.POST.get("roll")
        if roll.isdigit():
            
    

            try:
                student = Student.objects.get(roll=int(roll))
                subjects = Subject.objects.filter(student=student)
                print(student.name)
            except :
                subjects = "0"
                student = "0"
                print("no student found")
        else:
            subjects = "0"
            student = "0"
            print("no student found")
            
        context = {"subjects": subjects,"student":student,"roll":roll}
        return render(request,"result.html",context)
    roll = ""
    return render(request,"result.html",context={"student":"no","roll":roll})
def chromeex(request):
    return render(request, "chromeex.html")