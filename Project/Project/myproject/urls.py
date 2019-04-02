from django.urls import path, include
from .views import HomeView, CreateProjectView, ListProjectView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateProjectView.as_view(), name='create'),
    path('create/project/', ListProjectView.as_view(), name='projectlist'),
]
