from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['code_num', 'id_num', 'pname',
                    '_class', 'des', 'owner']
        exclude = ['created_by',]