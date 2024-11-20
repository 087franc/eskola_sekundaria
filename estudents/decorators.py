# decorators.py
from django.http import HttpResponseForbidden

def group_required(admin):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.groups.filter(name=admin).exists():
                return HttpResponseForbidden("You do not have permission to access this page.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
