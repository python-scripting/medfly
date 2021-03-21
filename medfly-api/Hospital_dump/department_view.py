from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital, Procedures as ProceduresModel, Department
from Hospital.serializers import HospitalSerializer, DepartmentSerializer
from Hospital.serializers import ProceduresInfoSerializer
from rest_framework.permissions import IsAuthenticated


class ManageDeparment(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		AllDepartments = Department.objects.all()
		serializer = DepartmentSerializer(AllDepartments, many=True)
		return Response(serializer.data)
	def post(self, request):
		data = json.loads(request.body)
		Department(Hosp_ID = data['body']['Hosp_ID'],Department_Name = data['body']['Department_Name']).save()
		return Response(status=status.HTTP_201_CREATED)
	def delete(self, request):		
		#data = json.loads(request)
		
		Department.objects.get(id=request.GET['ID']).delete()
		return Response(status=status.HTTP_201_CREATED)
