from django.urls import path
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/<int:category_id>", views.html_test, name="test"),
    path('test_check/<str:question_id>/<str:answer>/', views.test_check, name="test_check"),
    path('login/', views.login_page, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('create_question', views.create_question, name='create_question')
]