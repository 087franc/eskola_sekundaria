from django.contrib import admin

from estudents.models import *

# Register your models here.
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Teacher)