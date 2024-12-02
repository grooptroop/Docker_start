from django.contrib import admin
from django.urls import path
from .views import schedule_calendar, table_view, krasota, blackjack, kaz

urlpatterns = [
path('', blackjack, name='krasota'),
path('f', schedule_calendar, name='shedule'),
path('LAB', table_view, name='table'),
path('Fuf', kaz, name='Fuf'),
path('kaz', kaz, name='kaz'),

]