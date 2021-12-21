from django.contrib.auth import views as view
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('', view.LoginView.as_view(template_name='userfiles/login.html'), name='login'),
    path('login/', view.LoginView.as_view(template_name='userfiles/login.html'), name='login'),
	path('logout/', view.LogoutView.as_view(template_name='userfiles/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]
