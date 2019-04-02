from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    code_num = models.IntergerField()
    id_num = models.IntergerField()
    pname = models.CharField(max_length=300)
    _class = models.CharField(max_length=300)
    des = models.TextField()
    owner = models.CharField(max_length=300)

class SubProject(models.MOdel):
    owned_by = models.ForeignKey(Project, on_delete=models.CASCADE)
    code_num = models.IntergerField()
    id_num = models.IntergerField()
    cost = models.IntergerField()
    benefit = models.TextField()
    e_start_date = models.DateField() # ------> Estimated start time
    e_close_date = models.DateField()
    a_start_date = models.DateField()   # ----->  Actual start time
    a_close_date = models.DateField()
    leader = models.CharField(max_length=300)

class SubProjectAppriasal (models.Model):
    code_num = models.IntergerField()
    id_num = models.IntergerField()
    sid_num = models.IntergerField() #----> subproject identification number
    ap_date = models.DateField()    #----> appriases date
    delay_reason = models.TextField()  
    r_action = models.TextField()   # ----> remedial action taken
    a_name = models.CharField(max_length=300) # appriaser's name

class SubProjectCloseout (models.Model):
    code_num = models.IntergerField()
    id_num = models.IntergerField()
    sid_num = models.IntergerField() #----> subproject identification number
    close_num = models.IntergerField()
    c_date = models.DateField()    #----> closeout date
    remark = models.TextField()
     a_name = models.CharField(max_length=300) # appriaser's name



