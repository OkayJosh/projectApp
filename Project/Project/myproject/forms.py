from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['code_num', 'id_num', 'pname',
                    '_class', 'des', 'owner']
        exclude = ['created_by',]
        # labels = {
        #     'code_num': _('Project Code Number FGN or STA'),
        #     'id_num': _('Project Identification  Number'),
        #     'pname': _('Project Name'),
        #     '_class': _('Project Classification'),
        #     'des': _('Project Description'),
        #     'owner': _('Project Owner'),
        # }
        # help_texts = {
        #     'code_num': _('Project Code Number FGN or STA here'),
        #     'id_num': _('Project Identification  Number here'),
        #     'pname': _('Project Name here'),
        #     '_class': _('Project Classification here'),
        #     'des': _('Project Description here'),
        #     'owner': _('Project Owner here'),
        # }
        # error_messages = {
        #     'pname': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }