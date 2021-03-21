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
from usermanager.models import User
from usermanager.serializers import UserSerializer


class ManageHospitalUsers(APIView):
	def get(self, request):
		allUsers = User.objects.all().order_by("-id")
		
		serializer = UserSerializer(allUsers, many=True)
		return Response(serializer.data)