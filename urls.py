from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('success/', views.registration_success, name='success'),
    path('students/', views.student_list, name='student_list'),
    
]


