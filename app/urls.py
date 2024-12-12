from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('budget/', views.budget, name='budget'),
    path('expenses/', views.expenses, name='expenses'),
    path('summary/', views.summary, name='summary'),
    path('analysis/', views.analysis, name='analysis'),
    path('transactions/', views.transactions, name='transactions'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
