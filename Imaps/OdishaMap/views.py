from django.shortcuts import render

def timetable(request):
    return render(request, 'OdishaMap/timetable.html')