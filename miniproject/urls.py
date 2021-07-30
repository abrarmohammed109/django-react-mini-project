from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', views.career_list, name='career_list'),
# ]


urlpatterns = [
    path('careers/', views.CareerList.as_view(), name='career_list'),
    path('careers/<int:pk>', views.CareerDetail.as_view(), name='careers_detail'),
]

