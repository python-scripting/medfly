from django.db import models
from datetime import datetime
# Create your models here.



class Department(models.Model):
	Hosp_ID = models.CharField(max_length=100, null=True, blank=True)
	Department_Name = models.CharField(max_length=120, null=True, blank=True);
	def __str__(self):
		return self.Department_Name
#Hosp_ID
#Department_Name

class Role(models.Model):
	
	Role_ID = models.PositiveIntegerField()#admin 1, doctor
	Role_Name= models.CharField(max_length=20, null=True, blank=True)
	Department_ID  = models.PositiveIntegerField(default=0)
	Department_Name = models.CharField(max_length=100, null=True, blank=True)
	Permissions =  models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.Role_Name


class  Procedures(models.Model):
	
	Department_ID = models.PositiveIntegerField()
	Department_Name= models.CharField(max_length=120, null=True, blank=True)
	Procedure_Name= models.CharField(max_length=120, null=True, blank=True)
	Procedure_Status = models.CharField(max_length=20, default="Active")
	def __str__(self):
		return self.Procedure_Name

class Template(models.Model):
	
	Department_ID  = models.PositiveIntegerField() 
	Department_Name= models.CharField(max_length=120, null=True, blank=True);
	Procedure_Name= models.CharField(max_length=120, null=True, blank=True);
	Template_Name = models.CharField(max_length=120, null=True, blank=True);
	Template_Status = models.CharField(max_length=20, default="Create");# Create | Designed | Used
	def __str__(self):
		return self.Template_Name



class MenuItems(models.Model):
	
	Menu_Name= models.CharField(max_length=100)
	Menu_Path= models.CharField(max_length=100)
	Menu_Icon= models.CharField(max_length=100)
	Menu_Status= models.CharField(max_length=100, default="Active")
	 
	def __str__(self):
		return self.Menu_Name
class RoleBasedMenu():
	#[1,2]
	Menu_list= models.CharField(max_length=100, null=True, blank=True)
	User_id =  models.PositiveIntegerField()