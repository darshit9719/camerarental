from django.shortcuts import render
from django.contrib.auth.models import auth,User
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import camera
from django.conf import settings
import smtplib
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText
from smtplib import SMTPException

def home(request):
    return render(request,'index.html')
def send(request):
    message=request.POST['contact_message']
    email=request.POST['contact_email']
    message=message + "\nmy email=" + email
    send_mail('Contact From',message,settings.EMAIL_HOST_USER,['patil.vaibhavb.1999@gmail.com'])
    return render(request,'index.html')
def camerarequest(request):
    name=request.POST['contact_name']
    email=request.POST['contact_email']
    city=request.POST['city']
    timeduretion=request.POST['time']
    combotipe=request.POST['type']
    message="name=" +name +  "\ncity=" +city+ "\ntimeduretion="+ timeduretion + "\ncombotype="+ combotipe +"\nmy email=" + email
    send_mail('Camera_Rent_Request',message,settings.EMAIL_HOST_USER,['meetdobariya4321@gmail.com'])
    return render(request,'index.html')
def login1(request):
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return render(request,'index.html')
@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'index.html')
def register(request):
    return render(request,'register.html')
@csrf_exempt
def regist(request):
    if request.method=="POST":
        first_name=request.POST['name']
        last_name=request.POST['name']
        email=request.POST['email']
        username=request.POST['email']
        password=request.POST['password']
        password2=request.POST['re_password']
        mobile=request.POST['mobile_no']
        adress=request.POST['adrress']
        qulification=request.POST['qualification']
        if password==password2:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.save()
            rent=camera(first_name=first_name,email=email,Qulification=qulification,mobileno=mobile,adress=adress)
            rent.save()
        else:
            return render(request,'register.html')    
    return render(request,'login.html')