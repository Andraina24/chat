from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('chat/', views.handle_message, name='handle_message'),
    path('chat/message/', views.handle_message, name='handle_message'),
    #path('login', views.login, name='login'),
    #path('register', views.register, name='register'),
    #path('logout', views.logout, name='logout'),
]