from typing import Any
from django.urls import reverse
from rest_framework import generics 
from rest_framework.response import Response
import requests

from projects.models import Project
from projects.serializers import (
    ProjectSerializer, 
    ProjectCreateSerializer
    )

from django.views import generic


class ProjectListTempateView(generic.TemplateView):
    template_name = "projects/list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        url = reverse('api-project-list')
        host = "http://localhost:8000"
        project_list = requests.get(f"{host}{url}")
        context["project_list"] = project_list.json()

        return context

class ProjectsHomeTemplateView(generic.TemplateView):
    template_name = "projects/home.html"

    # def get(self, request, *args, **kwargs):
    #     # TODO remove the get_context_data below as we are redirecting traffic here
    #     return redirect('https://www.bunnyspaintings.com')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project"
        user_object = self.request.user or None
        is_logged_in = user_object.is_authenticated
        if is_logged_in:
            sitevisitor = user_object.username
        else:
            context["sitevisitor"] = "Guest"

        context["logged_in"] = is_logged_in
        return context



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


# class ProjectsCreateView(generics.GenericAPIView):
class ProjectsListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectCreateSerializer
    queryset = Project.objects.all()

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
