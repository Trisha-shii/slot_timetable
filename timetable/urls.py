from django.urls import path
from .views import slot_timetable

urlpatterns = [
    path('', slot_timetable, name='slot_timetable'),
]