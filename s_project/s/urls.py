from django.contrib import admin
from django.urls import path
from .views import schedule_calendar, table_view, krasota, blackjack, kaz

urlpatterns = [
path('', kaz, name='krasota'),
path('f', schedule_calendar, name='shedule'),
path('LAB', table_view, name='table'),
path('Fuf', krasota, name='Fuf'),
path('kaz', blackjack, name='kaz'),

]