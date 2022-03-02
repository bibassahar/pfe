from django.urls import path
from administration import views
urlpatterns = [
    path('files_list',views.files_list,name='files_list'),
    path('file_details/<str:namefile>/',views.file_details,name='file_details'),
]
