from django.shortcuts import render

def home(request):
    return render(request, 'demo.html')

def dashboard(request):
    return render(request, "dashboard.html")

def schemes(request):
    return render(request, "schemes.html")

def data_management(request):
    return render(request, "data_management.html")

def document_repository(request):
    return render(request, "document_repository.html")

def e_office(request):
    return render(request, "eoffice.html")

def correspondence(request):
    return render(request, "correspondence.html")

def reports_atr(request):
    return render(request, "reports_atr.html")

def monitoring(request):
    return render(request, "monitoring.html")

def user_role_management(request):
    return render(request, "users_roles.html")

def notifications_reminders(request):
    return render(request, "notifications_reminders.html")

def interdepartmental_sharing(request):
    return render(request, "data_sharing.html")

def security_audit_logs(request):
    return render(request, "security_audit_logs.html")