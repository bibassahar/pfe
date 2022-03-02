from django.urls import path
from administration import views
urlpatterns = [
    path('files_list',views.files_list,name='files_list'),
    path('details/<str:namefile>/',views.details_file,name='details'),
]
