from django.urls import path
from administration import views
urlpatterns = [
    path('admin',views.administrateur,name='admin'),
]
