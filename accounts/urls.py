from django.contrib import admin
from django.urls import path
from .views import account
from .views import admin
from .views import resources

urlpatterns = [
    path('', account.login, name='login'),
    path('student_portal', account.student_portal, name='student_portal'),
    path('questions', account.questions, name='questions'),
    path('faq', account.faq, name='faq'),
    path('answer', account.answers, name='answer'),
    path('logout', account.logout, name='logout'),

    path('login', admin.login, name='admin_login'),
    path('signup', admin.register, name="signup"),

    path('create_course', resources.create_course, name="create_course"),
    path('resources', resources.resources, name="resources"),
    path('course/<int:id>', resources.Course_Details, name="course"),
    path('course/module', resources.create_module, name="create_module"),


    path('logout', admin.logout, name='sign_out'),
]
