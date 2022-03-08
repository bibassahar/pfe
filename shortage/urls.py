from django.urls import path
from shortage import views
urlpatterns = [
    #Import Files
    path('upload',views.home,name='upload'), #To upload fils

    #CRUD Core
    path('core',views.core,name='core'), 
    path ('create_core',views.create_core,name='create_core'),
    path('update_core/<int:pk>/',views.update_core,name='update_core'),
    path('delete_core/<int:pk>/',views.delete_core,name='delete_core'),
]
