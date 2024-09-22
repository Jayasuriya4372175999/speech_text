"""from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient_details
from .forms import PatientDetailsForm

def index(request):
    return render(request, 'main/home.html', {})


def register(request):
    if request.method == 'POST':
        form = PatientDetailsForm(request.POST)
        if form.is_valid():
            patient = form.save()  # Save the patient and get the instance
            return redirect('success', patient_id=patient.id)
    else:
        form = PatientDetailsForm()
        
    return render(request, 'main/register.html', {'form': form})

def success(request, patient_id):
    patient = get_object_or_404(Patient_details, id=patient_id)
    return render(request, 'main/success.html', {'patient': patient})

def view_patient(request, patient_id):
    patient = get_object_or_404(Patient_details, id=patient_id)
    return render(request, 'main/view_patient.html', {'patient': patient})


# Search for patients based on name or phone number
def search(request):
    query_name = request.GET.get('name', '')
    query_phone = request.GET.get('phone', '')
    patients = Patient_details.objects.all()

    if query_name:
        patients = patients.filter(first_name__icontains=query_name)  # Search by name (case-insensitive)
    if query_phone:
        patients = patients.filter(phone_number__icontains=query_phone)  # Search by phone

    return render(request, 'view_patient.html', {'patients': patients})

# View individual patient details
def view_patient(request, patient_id):
    patient = get_object_or_404(Patient_details, id=patient_id)
    return render(request, 'view_patient.html', {'patient': patient})"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient_details
from .forms import PatientDetailsForm
import os
from django.conf import settings  # To access settings like BASE_DIR

def index(request):
    return render(request, 'main/home.html', {})

def register(request):
    if request.method == 'POST':
        form = PatientDetailsForm(request.POST)
        if form.is_valid():
            patient = form.save()  # Save the patient and get the instance
            phone_number = patient.phone_number
            base_path = os.path.join(r'F:\Python\PatientRecords')

    # Create the main folder for this patient using their phone number
            patient_folder = os.path.join(base_path, phone_number)
    
    # Create the folder if it does not exist
            os.makedirs(patient_folder, exist_ok=True)

    # Define the subfolders you want to create inside the patient's folder
            subfolders = ['Audio_Samples', 'Transcripts', 'Medical_Reports']

    # Create each subfolder inside the patient's folder
            for subfolder in subfolders:
                os.makedirs(os.path.join(patient_folder, subfolder), exist_ok=True)
            return redirect('success', patient_id=patient.id)
                

    else:
        form = PatientDetailsForm()
        
    return render(request, 'main/register.html', {'form': form})

def success(request, patient_id):
    patient = get_object_or_404(Patient_details, id=patient_id)
    return render(request, 'main/success.html', {'patient': patient})

# View individual patient details
def view_patient(request, patient_id):
    patient = get_object_or_404(Patient_details, id=patient_id)
    
    # Define the base path and get patient folder
    base_path = r'F:\Python\PatientRecords'
    patient_folder = os.path.join(base_path, patient.phone_number)
    
    # Initialize dictionaries to store files and folders
    files_and_folders = {'Documents': {'files': [], 'folders': []}, 
                         'Images': {'files': [], 'folders': []}, 
                         'Reports': {'files': [], 'folders': []}}

    # Check if patient folder exists
    if os.path.exists(patient_folder):
        # Iterate over subfolders
        for subfolder in files_and_folders.keys():
            subfolder_path = os.path.join(patient_folder, subfolder)
            if os.path.exists(subfolder_path):
                try:
                    # List files and directories in the subfolder
                    for item in os.listdir(subfolder_path):
                        item_path = os.path.join(subfolder_path, item)
                        if os.path.isfile(item_path):
                            files_and_folders[subfolder]['files'].append(item)
                        elif os.path.isdir(item_path):
                            files_and_folders[subfolder]['folders'].append(item)
                except Exception as e:
                    # Add debugging output for errors
                    print(f"Error reading items in {subfolder_path}: {e}")
            else:
                # Add debugging output if subfolder does not exist
                print(f"Subfolder does not exist: {subfolder_path}")
    else:
        # Add debugging output if patient folder does not exist
        print(f"Patient folder does not exist: {patient_folder}")

    return render(request, 'main/view_patient.html', {'patient': patient, 'files_and_folders': files_and_folders})
  
# Search for patients based on name or phone number
def search(request):
    query_name = request.GET.get('name', '')
    query_phone = request.GET.get('phone', '')
    patients = Patient_details.objects.all()

    if query_name:
        patients = patients.filter(first_name__icontains=query_name)  # Search by name (case-insensitive)
    if query_phone:
        patients = patients.filter(phone_number__icontains=query_phone)  # Search by phone

    return render(request, 'main/search_results.html', {'patients': patients})
