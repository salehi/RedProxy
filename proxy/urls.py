from django.urls import path

from .views import *

app_name = 'common'

urlpatterns = [
    path(r'', index, ),
]
