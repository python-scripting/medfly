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
#from Hospital.serializers import HospitalSerializer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


class ManageHospital(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		hospitals = Hospital.objects.all().order_by("-id")
		if request.GET.get('hospid', False):
			hospitals = Hospital.objects.filter(id=request.GET.get('hospid'))		
		serializer = HospitalSerializer(hospitals, many=True)
		return Response(serializer.data)
	def post(self, request):
		if request.method == 'POST':
			return Response(status=status.HTTP_200_OK)