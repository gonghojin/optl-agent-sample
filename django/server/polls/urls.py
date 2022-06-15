from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('error', views.error, name='error'),
    path('error-sqlite', views.sql_select, name='sqlite'),
]