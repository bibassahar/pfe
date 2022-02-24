from django import forms
from app.models import Core

class Myform(forms.ModelForm):
    class Meta:
        model = Core
        # fields = ['updated_by','plant','program','supplier','part_number','create','type_of_alert','requested_date','needed_quantity','production_comments','status','procurement_comments','closing_date','duration_of_the_event']
        fields = '__all__'
        