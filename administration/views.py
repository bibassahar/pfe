from re import match
from django.shortcuts import render
from shortage.models import MB52,SE16N_CEPC,SE16N_T001L,SE16N_T024,ZMM_CARNET_CDE_IS,ZRPFLG13

# Create your views here.
def files_list(request):
    return render(request,r'administration\files_list.html' )

def details_file(request,namefile):
    data=namefile.objects.all()
    
    return render(request,r'administration\details.html',{'data':data})
