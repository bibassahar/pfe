from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def administrateur(request):
    return render(request,r'administration\admin.html' )
