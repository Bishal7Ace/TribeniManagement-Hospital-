# Register your models here.
from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails, Receptionist
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class ReceptionistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Receptionist, ReceptionistAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)
