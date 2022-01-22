from django.shortcuts import render,redirect
from main.forms import PatientForm, DoctorForm, patient_discriptionForm
from main.models import Doctor,addPatient, patient_Discription



# Create your views here.
def Patient(request):
    if request.method =='POST':
        form=PatientForm(request.POST)
        
        patient=addPatient()
        
        if form.is_valid():
            Name=form.cleaned_data['patientName']
            patient.Patient_name=Name
            
            hospitalAddress=form.cleaned_data['Address']
            patient.Address=hospitalAddress
            

            phoneNumber=form.cleaned_data['phone']
            patient.phone=phoneNumber

            email=form.cleaned_data['email']
            patient.email=email

            assign_doctor=form.cleaned_data['assignDoctor']
            dr=Doctor.objects.get(first_name=assign_doctor)
            patient.assignDoctor=dr

            

            patient.save()
            # add=Hospital(h_name=Name,hAddress=hospitalAddress,phone=phoneNumber,email=email,assignDoctor=assign_doctor)
            # add.save()

            allEnrties=addPatient.objects.all()
            print(allEnrties)

        return render(request,"main/addDoctors.html",{'form':form})

    else:
        form=PatientForm()
    return render(request,"main/hospital.html",{'form':form})
def home(request):
    return render(request,'main/base.html')
def addDoctor(request):
    if request.method=='POST':
        form=DoctorForm(request.POST)
        doctors=Doctor.objects.all()
        doct=Doctor()

        if form.is_valid():
            # first_name=form.cleaned_data['doctorFirstName']
            # doct.first_name=first_name
            # last_name=form.cleaned_data['doctorLastName']
            # doct.last_name=last_name
            # dr_id=form.cleaned_data['DrId']
            # doct.DrId=dr_id
            # address=form.cleaned_data['Address']
            # doct.address=address
            # ph_number=form.cleaned_data['Phone']
            # doct.phone=ph_number
            # doct.save()
            form.save()
            return redirect('/show')  
            
            # doctor=Doctor(first_name=first_name,last_name=last_name,dr_id=dr_id,address=address,ph_number=ph_number)
            # doctor.save()

            # allEnrties=Doctor.objects.all()
            # print(allEnrties)

        return render(request,"main/show.html",{'doctorss':doctors})

    else:
        form=DoctorForm()
    return render(request,"main/addDoctors.html",{'form':form})
    
def patientDetails(response):
    if(response.method=='POST'):
        form=patient_discriptionForm(response.POST)
        pDm=patient_Discription()
        if form.is_valid():
            pName=form.cleaned_data['patientName']
            pDisease=form.cleaned_data['NameofDisease']
            usedMedicine=form.cleaned_data['useMedicine']
            useDiscription=form.cleaned_data['howtouseMedicine']
            discrtiption=patient_Discription(patientName=pName,diseaseName=pDisease,usedMedicine=usedMedicine,medicineUses=useDiscription)
            discrtiption.save()
            return redirect('/view') 

            print(patient_Discription.objects.last())

        return render(response,"main/patientDetails.html",{'form':form})
    else:
        form=patient_discriptionForm(response.POST)
        return render(response,"main/patientDetails.html",{'form':form})
def view(response):
    dis=patient_Discription.objects.all()
    return render(response,"main/view.html",{"disc":dis})

def show(request):  
    doctors = Doctor.objects.all()  
    return render(request,"main/show.html",{'doctorss':doctors})  
def edit(request, id):  
    doctor = Doctor.objects.get(id=id)  
    return render(request,'main/edit.html',{'doctorss':doctor})  
def update(request, id):
    id=int(id)
    if request.method=='POST':
        doctor = Doctor.objects.get(id = id)  
        a = DoctorForm(request.POST,instance=doctor)
        if a.is_valid(): 
            a.save()
            return redirect("/show")
        
        else:
            print (a.errors)
    return render(request, 'main/edit.html', {'doctorss': doctor}) 

def updatePatientDis(request,id):
    disc=patient_Discription.objects.get(id=id)
    form=patient_discriptionForm(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/view")
    else:
        print(form.errors)
    return render(request,'main/editpatient.html',{'dis':disc})

def edit2(request,id):
    patient_des=patient_Discription.objects.get(id=id)
    return render(request,'main/editpatient.html',{'dis':patient_des})
    
        
def destroy(request, id):  
    doctor = Doctor.objects.get(id=id)  
    doctor.delete()  
    return redirect("/show")  