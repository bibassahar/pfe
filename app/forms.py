from dataclasses import fields
from django import forms
from app.models import Core

class Myform(forms.ModelForm):
    class Meta:
        model = Core
        fields = '__all__'
        # fields = ['plant','program','supplier','part_number','create','type_of_alert','requested_date','needed_quantity','production_comments','status','procurement_comments','closing_date','duration_of_the_event']
        exclude =['created_on','created_by','deleted','deleted_by','deleted_on','updated_by','updated_on']
        widgets = {
            'requested_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'closing_date' : forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'created_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'deleted_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'updated_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        