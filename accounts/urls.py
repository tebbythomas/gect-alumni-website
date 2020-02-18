from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'), 
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),  
    #path('dashboard', views.dashboard, name='dashboard')
]
