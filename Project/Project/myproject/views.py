from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .forms import ProjectForm
from .models import Project


class HomeView(TemplateView):
    template_name = 'home.html'

class ListProjectView(ListView):
    template_name = 'project/list.html'
    model = Project
    content_type = None 

class CreateProjectView(CreateView):
    template_name = 'project/create.html'
    form_class =  ProjectForm
    success_url = 'project'
    content_type = None 

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        instance  = form.save(commit=False)
        instance.created_by = self.request.user
        instance.save()
        self.object = form.save()
        return super().form_valid(form)

