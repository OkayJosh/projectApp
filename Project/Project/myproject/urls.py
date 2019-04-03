from django.urls import path, include
from .views import (HomeView, CreateProjectView, ListProjectView,
                        ProfileProjectView )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateProjectView.as_view(), name='create'),
    path('create/profile/<int:pk>/<str:slug>', ProfileProjectView.as_view(), name='profile'),
    path('create/project/', ListProjectView.as_view(), name='list'),
]
