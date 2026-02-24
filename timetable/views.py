from django.shortcuts import render

def slot_timetable(request):
    return render(request, 'slot_timetable.html')