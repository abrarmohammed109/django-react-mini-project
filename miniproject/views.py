# views.py

from rest_framework import generics
from .serializers import CareerSerializer
from .models import Career

class CareerList(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Career


# def career_list(request):
#     careers = Career.objects.all().values('role', 'industry', 'comnpany') 
#     career_list = list(careers) 
#     return JsonResponse(career_list, safe=False) 