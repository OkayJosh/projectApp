from django.urls import path, include
from .views import (HomeView, CreateProjectView, ListProjectView,
                        ProfileProjectView, CreateSubProjectView )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateProjectView.as_view(), name='create'),
    path('create/subproject/', CreateSubProjectView.as_view(), name='subproject'),
    path('create/subproject/<int:pk>', CreateSubProjectView.as_view(), name='subproject'),
    path('create/profile/<int:pk>/<str:slug>', ProfileProjectView.as_view(), name='profile'),
    path('create/project/', ListProjectView.as_view(), name='list'),
]
