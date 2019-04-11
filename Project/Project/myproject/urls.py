from django.urls import path, include
from .views import (HomeView, CreateProjectView, ListProjectView,
                        ProfileProjectView, CreateSubProjectView, 
                        CreateSubProjectAppriasalView, CreateSubProjectCloseoutView,
                        CreateProjectFund, UpdateProjectView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('create/', CreateProjectView.as_view(), name='create'),

    path('create/subproject/', CreateSubProjectView.as_view(), name='subproject'),

    path('create/subproject/appriasal/<int:pk>/', CreateSubProjectAppriasalView.as_view(),
    name='appriasal'),

    path('create/subproject/closeout/<int:pk>/', CreateSubProjectCloseoutView.as_view(), 
    name='closeout'),

    path('create/subproject/<int:pk>/<slug:slug>/', CreateSubProjectView.as_view(), 
    name='subproject'),

    path('create/profile/<int:pk>/<slug:slug>/', ProfileProjectView.as_view(), 
    name='profile'),

    path('create/project/update/<int:pk>/<slug:slug>/', UpdateProjectView.as_view(), 
    name='update_project'),

    path('create/project/', ListProjectView.as_view(), name='list'),

    path('create/project/fund/<int:pk>/<slug:slug>/', CreateProjectFund.as_view(), name='fund'),
]
