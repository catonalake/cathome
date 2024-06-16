# from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics 

from rest_framework.response import Response

# delete this junk below
def home_view(request, *args, **kwargs):
    print('home_view \n')
    print(dir(request))

    # print(dir(request.body))

    body = request.body
    print('home_view \n')
    print(body)

    print('home_view \n')
    print('home_view \n')
    print('home_view \n')

    return JsonResponse({"message":"hello world"})


# class HomeView(View):
class HomeView(APIView):
    def get(self, request, *args, **kwargs):
        print('HomeView \n')
        print(dir(request))

        # print(dir(request.body))

        body = request.body

        print('HomeView \n')
        print(body)

        print('HomeView \n')
        print('HomeView \n')
        print('HomeView \n')
        return JsonResponse({"message":"hello world"})
    
