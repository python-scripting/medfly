from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital,PatientInfo as PatientInfoModel
from Hospital.serializers import HospitalSerializer, PatientInfoSerializer
from rest_framework.permissions import IsAuthenticated


class PatientInfo(APIView):
	permission_classes = (IsAuthenticated,)

	def get_object(self, pk):
		try:
			return PatientInfoModel.objects.get(pk=pk)
		except PatientData.DoesNotExist:
			raise Http404
	def get(self, request,  format=None):
		if request.GET['Pid']:
			pk = request.GET['Pid']
			PatientData = self.get_object(pk)
			serializer = PatientInfoSerializer(PatientData)
			return Response(serializer.data)
		else:
			PatientData = PatientInfoModel.objects.all()
			serializer = PatientInfoSerializer(PatientData)
			return Response(serializer.data)

