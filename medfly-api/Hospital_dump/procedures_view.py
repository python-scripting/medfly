from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital,Procedures as ProceduresModel
from Hospital.serializers import HospitalSerializer
from Hospital.serializers import ProceduresInfoSerializer
from rest_framework.permissions import IsAuthenticated

class ManageProcedures(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		allProcedures = ProceduresModel.objects.all().order_by("-id")
		print(allProcedures)
		serializer = ProceduresInfoSerializer(allProcedures, many=True)
		return Response(serializer.data)
	def post(self, request):
		#data = json.loads(request.body)
		if request.method == 'POST':
			#serializer = HospitalSerializer(data=request.data)			
			data = json.loads(request.body)
			hspid = data['Hosp_ID']
			dpid =  data["Department_ID"]
			dpname = data["Department_Name"]
			pname =  data["Procedure_Name"]
			psave = ProceduresModel(Hosp_ID=hspid,Department_ID=dpid,Department_Name=dpname, Procedure_Name=pname  ).save()

		#ProceduresModel(Department_ID=,Department_Name=,Procedure_Name=, ).save()
		return Response(status=status.HTTP_201_CREATED)
	def delete(self, request):		
		#data = json.loads(request)
		ProceduresModel.objects.get(id=request.GET['ID']).delete()
		return Response(status=status.HTTP_201_CREATED)
