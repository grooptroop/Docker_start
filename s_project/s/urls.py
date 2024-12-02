from django.contrib import admin
from django.urls import path
from .views import schedule_calendar, table_view, krasota

urlpatterns = [
path('', krasota, name='krasota'),
path('f', schedule_calendar, name='shedule'),
path('LAB', table_view, name='table'),

]