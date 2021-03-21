from django.db import models
from datetime import datetime
# Create your models here.

class Hospital(models.Model):
	"""docstring for Haspital"""
	Hosp_ID =models.CharField(max_length=100, null=True, blank=True)
	Name = models.CharField(max_length=100)
	Email = models.CharField(max_length=50)
	Mobile =models.PositiveIntegerField()
	Location=models.CharField(max_length=100)
	Having_Branch =models.BooleanField(default=False)
	Branch_Name =models.CharField(max_length=100, null=True, blank=True)  
	Branch_Type =models.CharField(max_length=100,default='Main')   #: Main or SubBranch
	Owner_Name= models.CharField(max_length=100)
	Logo= models.CharField(max_length=50, null=True, blank=True)
	Account_Type = models.CharField(max_length=20,  default="Demo") #Demo | Licensed
	Account_StartDate = models.DateField(default=datetime.now)
	Account_ExpiryDate = models.DateField(null=True, blank=True)
	Installation_Date  = models.CharField(max_length=20, null=True, blank=True)
	Admin_Username = models.CharField(max_length=20, null=True, blank=True)
	#Admin_Password
	Owner_Username = models.CharField(max_length=20, default="Medfly@admin")
	Owner_Password = models.CharField(max_length=20, default="Medyadmin")
	#Owner_Password
	Quoted  = models.CharField(max_length=20, null=True, blank=True)
	Finalised_Cost = models.CharField(max_length=20, null=True, blank=True)
	Payment_Mode = models.CharField(max_length=20, null=True, blank=True)
	Due  = models.CharField(max_length=20, null=True, blank=True)
	Paid_By = models.CharField(max_length=20, null=True, blank=True)
	Lead_by   = models.CharField(max_length=20, null=True, blank=True) #Executive Names
	Contact_Person  = models.CharField(max_length=20, null=True, blank=True)
	Payment_Process = models.CharField(max_length=20, null=True, blank=True) # : Monthly/Yearly/OneTime
	Total_Devices  = models.CharField(max_length=20, null=True, blank=True)
	Status   =models.CharField( max_length=10, default="Active")
	def __str__(self):
		return self.Name

class Device(models.Model):
	Hosp_ID =models.CharField(max_length=100, null=True, blank=True)
	Device_Id=  models.CharField(max_length=20, null=True, blank=True)
	def __str__(self):
		return self.Device_Id

class Department(models.Model):
	Hosp_ID = models.CharField(max_length=100, null=True, blank=True)
	Department_Name = models.CharField(max_length=120, null=True, blank=True);
	def __str__(self):
		return self.Department_Name
#Hosp_ID
#Department_Name

class Role(models.Model):
	Hosp_ID = models.CharField(max_length=100, null=True, blank=True)
	Role_ID = models.PositiveIntegerField()#admin 1, doctor
	Role_Name= models.CharField(max_length=20, null=True, blank=True)
	Department_ID  = models.PositiveIntegerField(default=0)
	Department_Name = models.CharField(max_length=100, null=True, blank=True)
	Permissions =  models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.Role_Name


class  Procedures(models.Model):
	Hosp_ID = models.CharField(max_length=100, null=True, blank=True)
	Department_ID = models.PositiveIntegerField()
	Department_Name= models.CharField(max_length=120, null=True, blank=True)
	Procedure_Name= models.CharField(max_length=120, null=True, blank=True)
	Procedure_Status = models.CharField(max_length=20, default="Active")
	def __str__(self):
		return self.Procedure_Name

class Template(models.Model):
	Hosp_ID = models.CharField(max_length=100, null=True, blank=True)
	Department_ID  = models.PositiveIntegerField() 
	Department_Name= models.CharField(max_length=120, null=True, blank=True);
	Procedure_Name= models.CharField(max_length=120, null=True, blank=True);
	Template_Name = models.CharField(max_length=120, null=True, blank=True);
	Template_Status = models.CharField(max_length=20, default="Create");# Create | Designed | Used
	def __str__(self):
		return self.Template_Name

class Report(models.Model):
    Hosp_ID= models.CharField(max_length=100, null=True, blank=True)
    Report_Name= models.CharField(max_length=100)
    Department_ID  = models.PositiveIntegerField()
    Department_Name = models.CharField(max_length=120, null=True, blank=True)
    Procedure_Name = models.CharField(max_length=120, null=True, blank=True)
    Template_ID  = models.PositiveIntegerField()
    Template_Name = models.CharField(max_length=120, null=True, blank=True)
    Parameter_Name= models.CharField(max_length=50)
    Parameter_Value= models.CharField(max_length=50)
    def __str__(self):
    	return self.Report_Name

class PatientInfo(models.Model):
    Hsp_Id = models.CharField(max_length=100, null=True, blank=True)
    Mf_Id= models.CharField(max_length=100)
    Patient_Name = models.CharField(max_length=100)
    Mobile = models.PositiveIntegerField()
    Age= models.PositiveIntegerField()
    Gender = models.CharField(max_length=100)
    Alt_Id = models.CharField(max_length=100, null=True, blank=True)
    Date  = models.CharField(max_length=100)
    Total_Visits  = models.PositiveIntegerField(default=1)
    def __str__(self):
    	return self.Patient_Name

class PatientRegistration(models.Model):
	Hsp_Id= models.CharField(max_length=100, null=True, blank=True)
	Mf_Id= models.CharField(max_length=100)
	Alt_Id= models.CharField(max_length=100)
	Procedure_Id = models.PositiveIntegerField()
	Procedure_Name = models.CharField(max_length=100)
	Doctor_Id = models.PositiveIntegerField()
	Doctor_Name= models.CharField(max_length=100)
	Anesthesian_Name= models.CharField(max_length=100)
	Referrer_Name= models.CharField(max_length=100)
	Status = models.CharField(max_length=100)
	Date = models.CharField(max_length=100)
	def __str__(self):
		return self.Mf_Id


class MediaFiles(models.Model):
	Hsp_Id= models.CharField(max_length=100, null=True, blank=True)
	Mf_Id= models.CharField(max_length=100)
	Procedure_Name = models.CharField(max_length=100) 
	File_Src= models.CharField(max_length=100)
	File_Thumbnail= models.CharField(max_length=100)
	File_Type= models.CharField(max_length=10,default="snap")
	File_Status= models.CharField(max_length=10, default="main") # (main | edited | )
	Annotation_Data= models.TextField(default='')
	def __str__(self):
		return self.File_Src

class MenuItems(models.Model):
	Hsp_Id= models.CharField(max_length=100, null=True, blank=True)
	Menu_Name= models.CharField(max_length=100)
	Menu_Path= models.CharField(max_length=100)
	Menu_Icon= models.CharField(max_length=100)
	Menu_Status= models.CharField(max_length=100, default="Active")
	 
	def __str__(self):
		return self.Menu_Name
class RoleBasedMenu():
	Hsp_Id= models.CharField(max_length=100, null=True, blank=True)
	#[1,2]
	Menu_list= models.CharField(max_length=100, null=True, blank=True)
	User_id =  models.PositiveIntegerField()
	Role_permissions =  models.PositiveIntegerField()