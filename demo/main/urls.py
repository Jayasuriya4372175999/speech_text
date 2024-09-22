from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('success/<int:patient_id>/', views.success, name='success'),
    path('view_patient/<int:patient_id>/', views.view_patient, name='view_patient'),
    path('search/', views.search, name='search'),
]
