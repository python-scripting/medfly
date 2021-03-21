 
from django.contrib import admin
from django.urls import path, include
#from  Hospital import    hospitals, procedures_view, department_view, roles_view, hospitals_users_view
from usermanager import views as userview
from rest_framework_simplejwt import views as jwt_views

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
	#path('hospital/', hospitals.ManageHospital.as_view()),
	#path('procedures/', procedures_view.ManageProcedures.as_view()),
    #path('department/', department_view.ManageDeparment.as_view()),
    #path('roles/', roles_view.Manageroles.as_view()),
    #path('allusers/', hospitals_users_view.ManageHospitalUsers.as_view()),
    #path('usermanageuser/',  userview.UserView.as_view()),   
    #path('login/', obtain_jwt_token, name='token_obtain_pair'),
    path('medlytoken/', verify_jwt_token, name='verify_jwt_token'),
    path('refresh/', refresh_jwt_token, name='refresh_jwt_token'),
    path('login/',userview.CustomTokenObtainPairView.as_view()),
   
]
