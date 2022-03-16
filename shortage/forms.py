from django import forms
from shortage.models import Core,CoreHistory
from crispy_forms.helper import FormHelper

class Myform(forms.ModelForm):
    class Meta:
        model = Core
        fields = '__all__'
        exclude =['created_on','created_by','deleted','deleted_by','deleted_on','updated_by','updated_on','status','closing_date']
        widgets = {
            'requested_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'closing_date' : forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'created_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'deleted_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'updated_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
class Form(forms.ModelForm):
     class Meta:
        model = CoreHistory
        fields = '__all__'
        exclude =['core','created_on','created_by','action']
        
   
        

           