from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_event, name='report_event'),
    path('report/success/', views.report_success, name='report_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
