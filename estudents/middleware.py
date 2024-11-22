# middleware.py
from django.contrib import messages
from django.shortcuts import redirect

class GroupRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define group-based URL prefixes
        if request.user.is_authenticated:
            if request.path.startswith('/admin/') and not request.user.groups.filter(name='admin').exists():
                return redirect('no_permission')
            if request.path.startswith('/teacher/') and not request.user.groups.filter(name='teachers').exists():
                return redirect('no_permission')
            if request.path.startswith('/student/') and not request.user.groups.filter(name='students').exists():
                return redirect('no_permission')
    
        return self.get_response(request)
