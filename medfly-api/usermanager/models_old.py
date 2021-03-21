from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User,BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
	use_in_migrations = True
	def create_user(self, fullname, mobile, password, is_active=True, is_staff=True, is_admin=False):
		if not mobile:
			raise ValueError('Mobile Number is required')
		if not password:
			raise ValueError('password is required')

		user_obj = self.model(fullname=fullname, mobile=mobile, password=password)
		user_obj.set_password(password)
		user_obj.admin	= is_admin
		user_obj.staff   = is_staff
		user_obj.active  = is_active

		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, hospid, fullname, mobile, roleId, role_name,  password):
		user = self.create_user(fullname, mobile,  mobile, roleId, role_name, password,is_staff=True,is_admin=False)
		#return user

	def create_superuser(self,hspId, fullname, mobile, roleId, role_name,  password):
		user = self.create_user(hspId, fullname, mobile, roleId, role_name,password, is_staff=True,is_admin=True)
		return user


class Menu(models.Model):
	hspId      = models.CharField(max_length=50,  null=True, blank=True)
	menu_name  = models.CharField(max_length=50,  null=True, blank=True)
	menu_icon  = models.CharField(max_length=50,  null=True, blank=True)
	menu_rout   = models.CharField(max_length=50,  null=True, blank=True)
	menu_state =  models.CharField(max_length=50,  null=True, blank=True)

class UserPermai(models.Model):
	userid = models.PositiveIntegerField(null=True, blank=True)
	permation_menu = models.CharField(max_length=100,  null=True, blank=True)
	permations     = models.PositiveIntegerField(default=0)

class User(AbstractBaseUser,PermissionsMixin):
	hspId      	= models.CharField(max_length=50,  null=True, blank=True)
	fullname   	= models.CharField(max_length=100, help_text='fullname is required',error_messages={'unique':'Please enter fullname'})
	mobile     	= models.CharField(max_length=50,unique=True, help_text='mobile number is required',error_messages={'unique':'Please enter mobile number'})
	roleId     	= models.PositiveIntegerField(null=True, blank=True)
	role_name   = models.CharField(max_length=50,  null=True, blank=True)
	department 	= models.PositiveIntegerField(null=True, blank=True)
	staff      	= models.BooleanField(default=True)
	admin      	= models.BooleanField(default=False)
	active     	= models.BooleanField(default=False)
	is_hadmin 	= models.BooleanField('hadmin status', default=False)
	is_sadmin 	= models.BooleanField('sadmin status', default=False)
	show_pwd    = models.CharField(max_length=100,  null=True, blank=True)
	is_active = models.BooleanField('Is active', default=True)	
	date_joined = models.DateTimeField('date joined', default=timezone.now)
	last_logout = models.DateTimeField(null=True)


	objects = UserManager()
	

	USERNAME_FIELD = 'mobile'
	REQUIRED_FIELDS=['hspId','fullname',  'roleId', 'role_name']

	def __str__(self):
		return self.fullname

	def get_fullname(self):
		return self.fullname

	def get_mobile(self):
		return self.mobile

	@property
	def is_superuser(self):
		return self.admin

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_active(self):
		return self.active

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perm(self, app_label):
		return True



class Meta:
	verbose_name = 'user'
	verbose_name_plural = 'users'
	swappable = "AUTH_USER_MODEL"

