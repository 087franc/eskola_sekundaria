from django.urls import path
from estudents.views import *

urlpatterns = [
    path('', index, name=('index'))
]