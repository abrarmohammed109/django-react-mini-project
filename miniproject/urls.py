from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.career_list, name='career_list'),
]