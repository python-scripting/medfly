from django.contrib import admin

# Register your models here.
from .models import Hospital, Device, Department, Role, Procedures, Template,Report,PatientInfo, PatientRegistration, MediaFiles, MenuItems

admin.site.register(Hospital)

admin.site.register(Device)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Procedures)
admin.site.register(Report)
admin.site.register(PatientInfo)
admin.site.register(PatientRegistration)
admin.site.register(MediaFiles)
admin.site.register(MenuItems)







