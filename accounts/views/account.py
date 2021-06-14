from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from ..models import Users, Questions, Answers, Courses

# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('student_portal')
        else:
            messages.error(request, "invalid credentials!!")
            return redirect('login')

    else:
        return render(request, "index.html")

def student_portal(request):
    courses = Courses.objects.all()
    return render(request, "student_portal.html", {'courses':courses})

def logout(request):
    auth.logout(request)
    messages.success(request, "logout successfully")
    return redirect("login")

def questions(request):
    user = request.user
    if request.method=="POST":
        question = request.POST['question']
        quiz = Questions.objects.create(quiz = question, user = user.email )
        quiz.save()
        messages.success(request, "Posted successfully")
        return redirect("student_portal")
    else:
        messages.error(request, "Error posting your question")
        return redirect("student_portal")

def faq(request):
    if request.method=="POST":
        question = request.POST['question']
        quiz = Questions.objects.create(quiz = question, user = user.email )
        quiz.save()
        messages.success(request, "Posted successfully")
        return redirect("student_portal")
    else:
        answers = Answers.objects.all()
        questions = Questions.objects.all()
        return render(request, "all_answers.html", {'questions':questions, 'answers':answers})

def answers(request):
    if request.method=="POST":
        answer = request.POST['answer']
        quiz_id = request.POST['quiz_id']
        
        answers = Answers()
        answers.answer = answer
        answers.quiz_id = quiz_id
        answers.user = request.user.email
        answers.save()
        # .objects.create(answer = answer, quiz_id = quiz_id, user = user.email )
        messages.success(request, "Answer saved")
        return redirect("faq")
    else:
        
        return render(request, "all_answers.html")