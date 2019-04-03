from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    code_num = models.IntegerField()#--------------->                                           Project Code number FGN or STA
    id_num = models.IntegerField()  #--------->                                                 Project main identification Number
    pname = models.CharField(max_length=300)# --------------->                                  Project name
    _class = models.CharField(max_length=300) #----------------->                               Classification of project
    des = models.TextField()                   #------------->                                  Description of project
    owner = models.CharField(max_length=300) #----------------------->                          Owner of the projec: the agency

    def __str__(self):
        return self.pname

class SubProject(models.Model):
    """
    This models the Project Registration info

    """
    owned_by = models.ForeignKey(Project, on_delete=models.CASCADE)
    spname = models.CharField(max_length=300, default="no name") #------------> sub project name
    scode_num = models.IntegerField() #-------------->                          Sub project code number
    id_num_beneficiary = models.CharField(max_length=300, default="no id")#     Idenfication number of beneficiary
    sid_num = models.IntegerField() #-------------->                            Sub project identification number
    cost = models.IntegerField()
    benefit = models.TextField() #-------------->                               The benefit of the project
    e_start_date = models.DateField() # ------>                                 Estimated start time
    e_close_date = models.DateField()
    a_start_date = models.DateField()   # ----->                                Actual start time
    a_close_date = models.DateField()
    leader = models.CharField(max_length=300) #----------->                     The leader of the subproject

class SubProjectAppriasal (models.Model):
    """
    This models the supproject appriasal info

    """
    owned_by = models.OneToOneField(SubProject, on_delete=models.CASCADE) 
    ap_date = models.DateField()    #---->                                      appriases date
    delay_reason = models.TextField()  
    r_action = models.TextField()   # ---->                                     remedial action taken
    a_name = models.CharField(max_length=300) #                                 appriaser's name

class SubProjectCloseout (models.Model):
    """
    This models the supproject closeout info

    """
    owned_by = models.OneToOneField(SubProject, on_delete=models.CASCADE) 
    id_num = models.IntegerField()
    sid_num = models.IntegerField() #---->                                      subproject identification number
    close_num = models.IntegerField()
    c_date = models.DateField()    #---->                                       closeout date
    remark = models.TextField() #
    a_name = models.CharField(max_length=300) #                                 appriaser's name

class ProjectFund(models.Model):
    """
    This models who will fund the project

    """
    owned_by = models.OneToOneField(Project, on_delete=models.CASCADE)
    name_funder = models.CharField(max_length=300) #--------->                   Name of the funding agency
    nature_funding = models.TextField()# ------------------->                    The nature of the funding
    amount = models.IntegerField()# ---------------------->                      Amount founded
    currency = models.CharField()# --------------------->                        Currency of the funded amount

    


