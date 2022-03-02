from django.shortcuts import render
from django.apps import apps


# Create your views here.
def files_list(request):
    models_name=apps.all_models['shortage']#to get all models in shortage

    return render(request,r'administration\files_list.html' ,{'models_name':models_name})

def file_details(request,namefile):
    Model=apps.get_model('shortage',namefile) #to get model from shortage
    
    data=Model.objects.values('file_number','uploaded_by','uploded_at')
    return render(request,r'administration\file_details.html',{'data':data})
