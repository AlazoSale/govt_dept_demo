
from django.urls import path 
from . import views

urlpatterns = [
	# path('', views.home, name='home')
    
    path("", views.dashboard, name="dashboard"),
    path("schemes/", views.schemes, name="schemes"),
    path("data/", views.data_management, name="data_management"),
    path("documents/", views.document_repository, name="document_repository"),
    path("e-office/", views.e_office, name="e_office"),
    path("correspondence/", views.correspondence, name="correspondence"),
    path("reports-atr/", views.reports_atr, name="reports_atr"),
    path("monitoring/", views.monitoring, name="monitoring"),
    path("users-roles/", views.user_role_management, name="users_roles"),
    path("notifications/", views.notifications_reminders, name="notifications_reminders"),
    path("data-sharing/", views.interdepartmental_sharing, name="data_sharing"),
    path("security-audit/", views.security_audit_logs, name="security_audit_logs"),
]
