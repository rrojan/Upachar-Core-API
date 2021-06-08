from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone_no', 'address', 'province', ]


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'phone_no', 
            'hospital_name', 
            'hospital_ward_name',
            'address', 
            'province',
            'occupation',
            'sex',
            'age',
            'day_of_pcr_positive',
            'PCR_CT_value',
            'vaccination_status',
            'prevalent_conditions',
            'stage_of_patient',
            'comorbidity_problems',
            'smoking_status',
            'assigned_to',
        ]

class AssignForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['assigned_to']