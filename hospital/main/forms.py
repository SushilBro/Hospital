from main.models import Doctor
from django import forms
class PatientForm(forms.Form):
    patientName=forms.CharField(label='Patient name',max_length=70)
    Address=forms.CharField(label='Address', max_length=100)
    phone=forms.CharField(label='Phone number',max_length=20)
    email=forms.EmailField(label='email',max_length=150)
    assignDoctor=forms.CharField(label='Assign Doctor', max_length=50)

class DoctorForm(forms.ModelForm):
    class Meta:  
        model = Doctor  
        fields = "__all__" 
    # doctorFirstName=forms.CharField(label='First Name',max_length=30)
    # doctorLastName=forms.CharField(label='Last Name',max_length=30)
    # DrId=forms.CharField(label='ID', max_length=100)
    # Address=forms.CharField(label='Address', max_length=100)
    # Phone=forms.CharField(label='Phone number',max_length=20)

class patient_discriptionForm(forms.Form):
    patientName=forms.CharField(label='Name of Patient',max_length=30)
    NameofDisease=forms.CharField(label='Name of Disease',max_length=100)
    useMedicine=forms.CharField(label='Given Medicine',max_length=50)
    howtouseMedicine=forms.CharField(label='How to use Medicine',max_length=200)

class EditPostForm(DoctorForm):
    class Meta(DoctorForm.Meta):
        fields = "__all__"





