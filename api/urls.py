from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.StudentList.as_view(),name='studentlist'),
    path('auth/',include('rest_framework.urls'))
]