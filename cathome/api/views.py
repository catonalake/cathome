# from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics 

from rest_framework.response import Response

from projects.models import Project
from projects.serializers import (
    ProjectSerializer, 
    ProjectCreateSerializer
    )


class ProjectsView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field="pk"


class ProjectsListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    # def get_queryset(self, *args, **kwargs):
    #     import pdb;pdb.set_trace()
    #     queryset = self.queryset.filter(name='Shani')
    #     return queryset


class ProjectsCreateView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        print('in get')
        print('in get')
        print('in get')
        print('in get')
        print('in get')
        print('in get')
        return Response({"nothing": "todo"})

    def post(self, request, *args, **kwargs):
        
        print('in post')
        print('in post')
        print('in post')
        print('in post')
        print('in post')
        print('in post')

        serializer = ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            print(f"instance {instance}")

            print({f"serializer.data {serializer.data}"})
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class ProjectsFormsFormatView(APIView):

    def get(self, request, *args, **kwargs):
        # thing = {"name": 'Project.objects.all().order_by("?").first().name'}
        # return JsonResponse(thing)

        model_data = Project.objects.all().order_by("?").first()
        json_data = model_to_dict(model_data, fields=['name', 'customer'])
        return Response(json_data)

class JunkProjectsView(APIView):
    def get(self, request, *args, **kwargs):
        # thing = {"name": 'Project.objects.all().order_by("?").first().name'}
        # return JsonResponse(thing)

        model_data = Project.objects.all().order_by("?").first()
        json_data = model_to_dict(model_data, fields=['name', 'customer'])
        return JsonResponse(json_data)
        # return JsonResponse({"name": Project.objects.all().order_by("?").first().name})





class ProjectsRandomView(APIView):
    def get(self, request, *args, **kwargs):
        # thing = {"name": 'Project.objects.all().order_by("?").first().name'}
        # return JsonResponse(thing)

        model_data = Project.objects.all().order_by("?").first()
        json_data = model_to_dict(model_data, fields=['name', 'customer'])
        return JsonResponse(json_data)
        # return JsonResponse({"name": Project.objects.all().order_by("?").first().name})


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
    
