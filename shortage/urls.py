from django.urls import path
from shortage import views
urlpatterns = [
    #Import Files
    path('upload',views.upload,name='upload'), #To upload fils

    #CRUD Core
    path('core',views.core,name='core'), 
    path ('core/create',views.create_core,name='create_core'),
    path('core/<int:pk>/update',views.update_core,name='update_core'),
    path('core/<int:pk>/delete',views.delete_core,name='delete_core'),
    path('core/<int:pk>/history/',views.core_history,name='core_history'),
]
