from django.urls import path
from app import views
urlpatterns = [
    path('index',views.home,name='index'),
    path ('create_core',views.create_core,name='create_core'),
    path('details',views.details,name='details'),
    path('delete_core/<int:pk>/',views.delete_core,name='delete_core'),
    path('update_core/<int:pk>/',views.update_core,name='update_core'),
]
