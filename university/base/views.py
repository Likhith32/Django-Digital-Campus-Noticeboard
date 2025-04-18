from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def notices(request):
    return render(request, 'notices.html')

def account(request):
    return render(request, 'account.html')

def about(request):  # Renamed to match the URL pattern
    return render(request, 'about.html')

def contact(request):  # Renamed to match the URL pattern
    return render(request, 'contact.html')

def exam_schedule(request):
    return render(request, 'exam_schedule.html')

def ity(request):
    return render(request, 'ity.html')