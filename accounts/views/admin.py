from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from ..models import Users, Courses
from django.template.loader import get_template, render_to_string

# Create your views here.
def register(request):
    if request.method=="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        username = request.POST['username']
        email = request.POST['email']
        password = Users.objects.make_random_password(length=10, allowed_chars='1235')
        # "pass123"
        
        if Users.objects.filter(email=email).exists():
            messages.error(request, "email exists!!")
            return redirect('signup')

        else:
            if Users.objects.filter(username=username).exists():
                messages.error(request, "username exists!!")
                return redirect('signup')
            else:
                user = Users() 

                user.name = request.POST['name']
                user.username = username
                user.email = email
                user.phone =  phone 
                # activation_code = Users.objects.make_random_password(length=10, allowed_chars='1235')
                user.password = make_password(password)
                
                user.save()
            
                
                subject = 'Your initiall password' 
                message = render_to_string('admin/adm_templates/password-email.html', {'password': password})
                from_email = 'donotreply.course.com'
                to = user.email
                send_mail(subject,message,from_email,[to] ,fail_silently=False, )
                
                messages.success(request,'Registered Successfully!!')
                return redirect("signup")  
                
                
    else:
        return render(request,"admin/adm_templates/sign_up.html")
        
def login(request):
    if request.method=="POST":
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Loadm_templatesgged in successfully!!")
            return redirect('signup')
        else:
            messages.error(request, "invalid credentials!!")
            return redirect('admin_login')

    else:
        return render(request, "admin/adm_templates/adminlogin.html")

def logout(request):
    auth.logout(request)
    messages.success(request, "logout successfully")
    return redirect("admin_login")