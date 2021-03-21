from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital,Procedures as ProceduresModel, Role
from Hospital.serializers import RoleSerializer


class Manageroles(APIView):
	def get(self, request):
		roles = Role.objects.all().order_by("-id")		
		serializer = RoleSerializer(roles, many=True)
		return Response(serializer.data)
		
	def post(self, request):
		if request.method == 'POST':
			data = json.loads(request.body)
			Role(Hosp_ID= data['Hosp_ID'], 
				Role_ID = 1,
				Role_Name = data['Role_Name'],
				Permissions = 0
	        ).save()
			return Response(status=status.HTTP_201_CREATED)
	def delete(self, request):
		Role.objects.get(id=request.GET['roleid']).delete()
		return Response(status=status.HTTP_201_CREATED)


 