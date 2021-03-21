from django.forms import widgets
from rest_framework import serializers
from .models import Hospital,Device,Department, PatientInfo, Procedures, MenuItems,Role


# Create your tests here.

class HospitalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hospital
		fields ='__all__' # ['id', 'Hosp_ID', 'Name', 'Email', 'Mobile', 'Location', 'Account_Type','Owner_Username','Owner_Password','Account_StartDate', 'Status']


class DeviceSerializer(serializers.ModelSerializer):
	"""docstring for Device"""
	class Meta:
		model = Device
		fields = ['id', 'Hosp_ID', 'Device_Id']

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = ['id', 'Hosp_ID', 'Department_Name']


class ProceduresSerializer(serializers.ModelSerializer):
	"""docstring for Device"""
	class Meta:
		model = Procedures
		fields = ['id', 'Department_ID', 'Department_Name', 'Procedure_Name', 'Procedure_Status']



class PatientInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientInfo
		fields = ['id', 'Hsp_Id','Mf_Id', 'Patient_Name', 'Mobile', 'Age', 'Gender', 'Alt_Id', 'Date', 'Total_Visits']

class ProceduresInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Procedures
		fields ='__all__'

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields ='__all__'

