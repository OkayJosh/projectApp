from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Project(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    code_number = models.IntegerField()#--------------->                                           Project Code number FGN or STA
    identification_number = models.IntegerField()  #--------->                                                 Project main identification Number
    name = models.CharField(max_length=300, default="Name of the Project", blank=True, null=True)
    slug = models.SlugField(max_length=300,
                            verbose_name = "slug")# --------------->                                  Project name
    project_class = models.CharField(max_length=300) #----------------->                               Classification of project
    description = models.TextField()                   #------------->                                  Description of project
    owner = models.CharField(max_length=300) #----------------------->                          Owner of the projec: the agency

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Project, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class SubProject(models.Model):
    """
    This models the SubProject Registration info

    """
    owned_by = models.ForeignKey(Project, on_delete=models.CASCADE)
    subproject_name = models.CharField(max_length=300, default="subproject name") #------------> sub project name
    subprject_code_number = models.IntegerField() #-------------->                          Sub project code number
    idenfication_number_of_beneficiary = models.CharField(max_length=300, default="no id")#     Idenfication number of beneficiary
    subproject_idenfication_number = models.IntegerField() #-------------->                            Sub project identification number
    cost = models.IntegerField()
    benefit = models.TextField() #-------------->                               The benefit of the project
    estimated_start_date = models.DateField() # ------>                                 Estimated start time
    estimated_close_date = models.DateField()
    actual_start_date = models.DateField()   # ----->                                Actual start time
    actual_close_date = models.DateField()
    leader = models.CharField(max_length=300) #----------->                     The leader of the subproject

class SubProjectAppriasal(models.Model):
    """
    This models the supproject appriasal info

    """
    owned_by = models.OneToOneField(SubProject, on_delete=models.CASCADE, blank=True, null=True) 
    appriase_date = models.DateField()    #---->                                      appriases date
    delay_reason = models.TextField()  
    remedial_action = models.TextField()   # ---->                                     remedial action taken
    appriaser_name = models.CharField(max_length=300) #                                 appriaser's name

class SubProjectCloseout(models.Model):
    """
    This models the supproject closeout info

    """
    owned_by = models.OneToOneField(SubProject, on_delete=models.CASCADE, blank=True, null=True) 
    identification_number = models.IntegerField()
    subproject_identification_number = models.IntegerField() #---->                                      subproject identification number
    closeout_number = models.IntegerField()
    closeout_date = models.DateField()    #---->                                       closeout date
    remark = models.TextField() #
    appriaser_name = models.CharField(max_length=300) #                                 appriaser's name

class ProjectFund(models.Model):
    """
    This models funding for the project

    """
    owned_by = models.OneToOneField(Project, on_delete=models.CASCADE)
    name_funder = models.CharField(max_length=300) #--------->                   Name of the funding agency
    nature_funding = models.TextField()# ------------------->                    The nature of the funding
    amount = models.IntegerField()# ---------------------->                      Amount founded
    currency = models.CharField(max_length=300)# --------------------->                        Currency of the funded amount

    


