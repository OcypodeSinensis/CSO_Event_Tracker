from django.urls import path
from . import views
from .views_export import export_events_xlsx

urlpatterns = [
    path('report/', views.report_event, name='report_event'),
    path('report/success/', views.report_success, name='report_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("export/xlsx/", export_events_xlsx, name="export_xlsx"),
    path('action/add/', views.add_action, name='add_action'),
    path('action/success/', views.action_success, name='action_success'),
]
