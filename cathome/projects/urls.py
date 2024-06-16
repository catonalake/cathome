from django.urls import path

from projects.views import (
    ProjectsView,
    ProjectsListCreateView,
    ProjectsListView,
    ProjectsHomeTemplateView,
    ProjectListTempateView,
    )

urlpatterns = [
    path('home/', ProjectsHomeTemplateView.as_view()),
    path('viewlist/', ProjectListTempateView.as_view()),
    path('<int:pk>/', ProjectsView.as_view()),
    path('create/', ProjectsListCreateView.as_view()),
    path('list/', ProjectsListView.as_view(), name='api-project-list'),
]