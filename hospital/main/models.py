from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
# Create your models here.


class Doctor(models.Model):
    
    first_name=models.CharField(max_length=200,blank=True)
    last_name=models.CharField(max_length=200,blank=True)
    address=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.first_name
      
    # def __str__(self, *args, **kwargs):
    #     field_values = []
    #     for field in self._meta.get_fields():
    #         field_values.append(str(getattr(self, field.name, '')))
    #     return ' '.join(field_values)

class addPatient(models.Model):
    # date = models.DateTimeField(auto_now=False, auto_now_add=False, unique=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name="hospital",null=True)
    Patient_name=models.CharField(max_length=200)
    Address=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=150)
    assignDoctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.h_name
    # def __str__(self):
    #       return '%s %s' % (self.h_name, self.hAddress,self.phone,self.email,self.assignDoctor)
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class patient_Discription(models.Model):
    
    patientName=models.CharField(max_length=70)
    usedMedicine=models.CharField(max_length=100)
    diseaseName=models.CharField(max_length=200)
    medicineUses=models.CharField(max_length=100)
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

