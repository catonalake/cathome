from django.urls import path, include

from api.views import (
    HomeView, 
    home_view, 
    )

urlpatterns = [
    path('projects/', include('projects.urls')),
    # junk items below
    path('class', HomeView.as_view()),
    path('func', home_view),
]