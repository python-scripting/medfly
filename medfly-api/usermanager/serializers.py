# users/serializers.py
from rest_framework import serializers
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
		data.update({'displayName': self.user.fullname})
		data.update({'about': "MedflyManagemnet"})
		data.update({'photoURL': ''})
		data.update({'status': 'Available'})
		data.update({'userRole': 'sadmin'})
		data.update({'id': self.user.id})
		data.update({'hspId': self.user.hspId})
		data.update({'mobile': self.user.mobile})
		data.update({'is_hadmin': self.user.is_hadmin})
		data.update({'is_sadmin': self.user.is_sadmin})
		return data