from django.urls import path
from .views import insert_vendor,find_vendor

app_name = 'service'

urlpatterns = [

    path('insert/', insert_vendor, name='insert_vendor'),
    path('find/', find_vendor, name='find_vendor'),
]
