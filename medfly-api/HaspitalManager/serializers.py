
from django.forms import widgets
from rest_framework import serializers
from .models import Hospital,Device,Department, PatientInfo, Procedures, MenuItems,Role



class HospitalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hospital
		fields ='__all__' # ['id', 'Hosp_ID', 'Name', 'Email', 'Mobile', 'Location', 'Account_Type','Owner_Username','Owner_Password','Account_StartDate', 'Status']
	