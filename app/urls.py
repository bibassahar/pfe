from django.urls import path
from app import views
urlpatterns = [
    path('index',views.home,name='index'),
    path ('corform',views.coreform,name='corform'),
]
