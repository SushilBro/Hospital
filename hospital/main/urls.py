from main import views
from django.urls import path
urlpatterns=[
path('hospital/',views.Patient,name='hospital'),
path('',views.home),
path('addDoctors/',views.addDoctor,name='addDoctor'),
path('patientDetails/',views.patientDetails,name='patientDetails'),
path('view/',views.view,name='ViewPatients'),
path('show/',views.show),  
path('edit/<int:id>', views.edit),  
path('update/<int:id>', views.update),  
path('edit2/<int:id>',views.edit2),
path('updatePatientDiscription/<int:id>',views.updatePatientDis),
path('delete/<int:id>', views.destroy),  
]
