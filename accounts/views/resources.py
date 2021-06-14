from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from ..models import Users, Courses, Course_Modules
from django.template.loader import get_template, render_to_string


# resources views
def create_course(request):
    if request.method=="POST":
        courseName = request.POST['course-name']
        user = request.user.email
        if Courses.objects.filter(course_name=courseName).exists():
            messages.error(request, "Course exists!!")
            return redirect('create_course')

        else:
            course = Courses() 
            course.course_name = courseName
            course.user_created = user  
            course.save()
            messages.success(request, "Saved successfully!")
            return redirect('create_course')

    else:
        return render(request, "admin/adm_templates/create_course.html")

def resources(request):
    courses = Courses.objects.all()
    return render(request, "admin/adm_templates/create_resources.html", {"courses":courses})

def Course_Details(request,id):
    courses = Courses.objects.all()
    course = Courses.objects.get(id=id)
    course_modules = Course_Modules.objects.all()
    return render(request, "admin/adm_templates/course.html", {"course":course, "courses":courses, "course_modules": course_modules })

def create_module(request):
    if request.method=="POST":
        moduleName = request.POST['module_name']
        description = request.POST['description']
        course_id = request.POST['courseId']
        link = request.POST['link']

        user = request.user.email

        course_Modules = Course_Modules() 
        course_Modules.moduleName = moduleName
        course_Modules.description = description
        course_Modules.course_id = course_id
        course_Modules.link = link
        course_Modules.user_created = user  
        course_Modules.save()
        messages.success(request, "Saved successfully!")
        return redirect('course', id=course_id)

    else:
        course_modules = Course_Modules.Objects.all()
        # return redirect('course', id=course_id, {"course_modules": course_modules})
        return redirect(request, "admin/adm_templates/course.html")
        # ,{"course_modules": course_modules})

