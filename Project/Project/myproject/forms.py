from django.forms import ModelForm
from .models import ( Project, SubProject, SubProjectAppriasal,
                        SubProjectCloseout, ProjectFund )


class ProjectForm(ModelForm):
    """
    The Project Form
    """
    class Meta:
        model = Project
        fields = ['code_num', 'id_num', 'slug',
                    '_class', 'des', 'owner']
        exclude = ['created_by',]

        field_classes = "pink darken-1"

class SubProjectForm(ModelForm):
    """
    The Subproject Form
    """
    class Meta:
        model = SubProject
        exclude =['owned_by']

class SubProjectAppriasalForm(ModelForm):
    """
    The SubProject Appraisal Form
    """

    class Meta:
        model = SubProjectAppriasal
        exclude =['owned_by']

class SubProjectCloseoutForm (ModelForm):
    """
    The SubProject close out Form

    """
    class Meta:
        model = SubProjectCloseout
        exclude = ['owned_by']

class ProjectFundForm(ModelForm):
    class Meta:
        model = ProjectFund
        exclude =['owned_by']