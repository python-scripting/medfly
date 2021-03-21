from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from usermanager.models import UserManager
# Create your views here.
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
import json

from usermanager import models 

from . import  serializers
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from usermanager.models import  User
from .serializers import CustomTokenObtainPairSerializer

from django.views.decorators.csrf import csrf_protect
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 

class UserView(APIView):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	#permission_classes = [IsAuthenticated]
	#permission_classes = (IsAuthenticated, ) 
	def get(self, request):
		print(request)
		queryset =   User.objects.all()
		serializer = serializers.UserSerializer(queryset, many=True)
		#serializer = HospitalSerializer(hospitals, many=True)
		return Response(serializer.data)

	def post(self, request):
		data = json.loads(request.body) 
		
		"""user(hspId      	=  data['Hosp_ID'],
		fullname   	=  data['Hosp_ID'],
		mobile     	= data['Hosp_ID'],
		roleId     	=  data['Hosp_ID'],
		role_name   = data['Hosp_ID'],
		department 	= data['Hosp_ID'],
		).save()"""
		
		User.objects.create_staffuser(data['Hosp_ID'],data['fullname'],data['mobile'], data['roleId'],data['role_name'], data['password']);
										#hspId, fullname, mobile, roleId, role_name,password

		queryset =  User.objects.all()
		serializer = serializers.UserSerializer(queryset, many=True)
		#serializer = HospitalSerializer(hospitals, many=True)
		return Response(serializer.data)

class UserLogin(APIView):
	def get(self, request):
		return Response(request.GET)


	def post(self, request):
		return Response(request.POST)


class CustomTokenObtainPairView(TokenObtainPairView):
	serializer_class = CustomTokenObtainPairSerializer
	token_obtain_pair = TokenObtainPairView.as_view()
