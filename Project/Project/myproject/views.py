from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import (ProjectForm, SubProjectForm, SubProjectAppriasalForm,
                    SubProjectCloseoutForm, ProjectFundForm)
from .models import Project, SubProject


class HomeView(ListView):
        template_name = 'home.html'
        model = Project
        content_type = None 

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['projects'] = Project.objects.all()[:5]
                return context

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

class UpdateProjectView(UpdateView):
        model = Project
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'project/update.html'
        form_class = ProjectForm
        success_url = '/create/project'

class ProfileProjectView(DetailView):
        """
        The goal is to have a one stop page for editing and veiwing project related information

        including a table for subprojects
        """
        template_name = 'project/profile.html'
        model = Project
        content_type = None 
        pk_url_kwarg = 'pk' 
        query_pk_and_slug = True
        slug_url_kwarg = 'slug'

        def get_context_data(self, **kwargs):
                project = Project.objects.get(id=self.kwargs['pk'])
                context = super().get_context_data(**kwargs)
                context['subprojects'] = SubProject.objects.filter(owned_by=project)[:5]
                return context

class CreateSubProjectView(CreateView):
        template_name = 'subproject/create.html'
        form_class =  SubProjectForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = '/create/project'
        # pattern_name = 'Profile'
        # success_url = reverse_lazy('profile', kwargs={'pk': 'pk','slug': 'slug'})

        # def get_redirect_url(self):
        #         """
        #         Return the URL redirect to. Keyword arguments from the URL pattern
        #         match generating the redirect request are provided as kwargs to this
        #         method.
        #         """
        #         url = reverse(self.pattern_name)
        #         url = "%s/%s/%s" % (url, self.pk, self.slug)
        #         return super().url


        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                project = Project.objects.get(id=self.kwargs['pk']) # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = project
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class CreateSubProjectAppriasal(CreateView):
        template_name = 'subproject/appriasal.html'
        form_class =  SubProjectAppriasalForm
        success_url = '/create/project'
        content_type = None 
        pk_url_kwarg = 'pk'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                subproject = SubProject.objects.get(id=self.kwargs['pk']) # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = subproject
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateSubProjectAppriasal(UpdateView):
        template_name = 'subproject/updateappriasal.html'

class CreateSubProjectCloseout(CreateView):
        template_name = 'subproject/closeout.html'
        form_class =  SubProjectCloseoutForm
        success_url = '/create/project'
        content_type = None
        pk_url_kwarg = 'pk' 

class UpdateSubProjectCloseout(UpdateView):
        template_name = 'subproject/updatecloseout.html'

class CreateProjectFund(CreateView):
        template_name ='project/fund.html'
        form_class =  ProjectFundForm
        content_type = None 
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        # success_url = reverse_lazy('profile', ['pk', 'slug'])

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                project = Project.objects.get(id=self.kwargs['pk']) # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = project
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateProjectFund(UpdateView):
                template_name ='project/updatefund.html'

### i still need to implement a way in which the subproject scope will get the project in question