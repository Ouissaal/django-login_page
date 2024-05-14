from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page),
    path('sign_up/', views.show_signup, name='sign_up')
]
