from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import (ProjectForm, SubProjectForm, SubProjectAppriasalForm,
                    SubProjectCloseoutForm, ProjectFundForm)
from .models import Project, SubProject


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
        """
        If the form is valid, save the associated model.

        """
        instance  = form.save(commit=False)
        instance.created_by = self.request.user
        instance.save()
        self.object = form.save()
        return super().form_valid(form)

class ProfileProjectView(DetailView):
    """
    The goal is to have a one stop page for editing and veiwing project related information
    
    """
    template_name = 'project/profile.html'
    model = Project
    content_type = None 
    pk_url_kwarg = 'pk' 
    query_pk_and_slug = True
    slug_url_kwarg = 'slug'

class CreateSubProjectView(CreateView):
    template_name = 'subproject/create.html'
    form_class =  SubProjectForm
    success_url = 'project'
    content_type = None
    pk_url_kwarg = 'pk'  

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        project = Project.objects.get(pk)
        instance  = form.save(commit=False)
        instance.owned_by = project
        instance.save()
        self.object = form.save()
        return super().form_valid(form)

class CreateSubProjectAppriasal(CreateView):
        template_name = 'subproject/appriasal.html'
        form_class =  SubProjectAppriasalForm
        success_url = 'project'
        content_type = None 

class UpdateSubProjectAppriasal(UpdateView):
        template_name = 'subproject/updateappriasal.html'

class CreateSubProjectCloseout(CreateView):
        template_name = 'subproject/closeout.html'
        form_class =  SubProjectCloseoutForm
        success_url = 'project'
        content_type = None 

class UpdateSubProjectCloseout(UpdateView):
        template_name = 'subproject/updatecloseout.html'

class CreateProjectFund(CreateView):
        template_name ='project/fund.html'
        form_class =  ProjectFundForm
        success_url = 'project'
        content_type = None 

class UpdateProjectFund(UpdateView):
        template_name ='project/updatefund.html'