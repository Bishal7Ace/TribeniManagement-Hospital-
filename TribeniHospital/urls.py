from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
   path('',views.home_view,name='home'),
   path('aboutus',views.aboutus_view,name='aboutus'),
   path('contactus',views.contactus_view,name='contactus'),
   path('department',views.department_view,name='department'),
   
   path('adminclick', views.adminclick_view, name='adminclick'),
   path('doctorclick', views.doctorclick_view, name='doctorclick'),
    path('patientclick', views.patientclick_view, name='patientclick'),
    path('receptionistclick', views.receptionistclick_view, name='receptionistclick'),
    
    path('adminsignup', views.admin_signup_view, name='adminsignup'),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view, name='patientsignup'),
    path('receptionistsignup', views.receptionist_signup_view, name='receptionistsignup'),
   
    path('adminlogin/', LoginView.as_view(template_name='adminlogin.html'), name='adminlogin'),
    path('doctorlogin/', LoginView.as_view(template_name='doctorlogin.html'), name='doctorlogin'),
    path('patientlogin/', LoginView.as_view(template_name='patientlogin.html'), name='patientlogin'),
    path('receptionistlogin/', LoginView.as_view(template_name='receptionistlogin.html'), name='receptionistlogin'),
    
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='home.html'),name='logout'),
    
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    
    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),

    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),
    
    path('admin-receptionist', views.admin_receptionist_view,name='admin-receptionist'),
    path('admin-view-receptionist', views.admin_view_receptionist_view,name='admin-view-receptionist'),
    path('delete-receptionist-from-hospital/<int:pk>', views.delete_receptionist_from_hospital_view,name='delete-receptionist-from-hospital'),
    path('update-receptionist/<int:pk>', views.update_receptionist_view,name='update-receptionist'),
    path('admin-add-receptionist', views.admin_add_receptionist_view,name='admin-add-receptionist'),
    path('admin-approve-receptionist', views.admin_approve_receptionist_view,name='admin-approve-receptionist'),
    path('approve-receptionist/<int:pk>', views.approve_receptionist_view,name='approve-receptionist'),
    path('reject-receptionist/<int:pk>', views.reject_receptionist_view,name='reject-receptionist'),
    
    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
    
    path('admin-inventory', views.admin_inventory_view,name='admin-inventory'),
    path('inventory-list/', views.inventory_list, name='inventory-list'),
    path('add-inventory-expense/', views.add_inventory_expense, name='add-inventory-expense'),
    path('add-inventory-usage/', views.add_inventory_usage, name='add-inventory-usage'),
]

#---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),

    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]

#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),
]

 #---------FOR RECEPTIONIST RELATED URLS-------------------------------------
urlpatterns +=[
      path('receptionist-dashboard', views.receptionist_dashboard_view,name='receptionist-dashboard'),
      
      path('receptionist-patient', views.receptionist_patient_view,name='receptionist-patient'),
      path('receptionist-view-patient', views.receptionist_view_patient_view,name='receptionist-view-patient'),
      path('receptionist-update-patient/<int:pk>', views.receptionist_update_patient_view,name='receptionist-update-patient'),
      path('receptionist-add-patient', views.receptionist_add_patient_view,name='receptionist-add-patient'),
      path('receptionist-discharge-patient', views.receptionist_discharge_patient_view,name='receptionist-discharge-patient'),
      path('receptionist-paper-discharge-patient/<int:pk>', views.receptionist_paper_discharge_patient_view,name='receptionist-paper-discharge-patient'),
      path('receptionist-download-pdf/<int:pk>', views.receptionist_download_pdf_view,name='receptionist-download-pdf'),
      
      path('receptionist-appointment', views.receptionist_appointment_view,name='receptionist-appointment'),
      path('receptionist-view-appointment', views.receptionist_view_appointment_view,name='receptionist-view-appointment'),
      path('receptionist-add-appointment', views.receptionist_add_appointment_view,name='receptionist-add-appointment'),
 ]
