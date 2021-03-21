from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets,generics
import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hospital
from Hospital.serializers import HospitalSerializer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

class ManageHospital(APIView):
	#permission_classes = (IsAuthenticated,)
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		hospitals = Hospital.objects.all().order_by("-id")
		if request.GET.get('hospid', False):
			hospitals = Hospital.objects.filter(id=request.GET.get('hospid'))		
		serializer = HospitalSerializer(hospitals, many=True)
		return Response(serializer.data)
	def post(self, request):
		if request.method == 'POST':
			#serializer = HospitalSerializer(data=request.data)			
			data = json.loads(request.body)
			hospital_branch_having= data['hospital_branch_having']
			hospital_branch_type= 	data['hospital_branch_type']
			Name 				= 	data['Name']
			Eamail 				= 	data['Email']
			Mobile 				= 	data['Mobile']
			Location			= 	data['Location']
			Account_Type 		=   data['Account_Type']
			Owner_Username 		=   data['Owner_Username']
			Owner_Password 		=   data['Owner_Password']
			Account_StartDate =     data['Account_StartDate']
			Status 				=   data['Status']
			hosptial = Hospital(Name = Name,
				Email = Eamail,
				Mobile =Mobile,
				Location=Location,
				Having_Branch  = hospital_branch_having,
				Branch_Name   = Name,
				Branch_Type   =hospital_branch_type,   #: Main or SubBranch
				Owner_Name    = hospital_branch_type+"_Admin",
				Account_Type = Account_Type,				
				Admin_Username = Mobile)
			hosptial.save()			
			return Response(status=status.HTTP_201_CREATED)
