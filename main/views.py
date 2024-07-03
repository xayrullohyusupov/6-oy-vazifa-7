from django.shortcuts import render
from . import models

def index(request):
    info = models.Info.objects.all()
    best = models.Best.objects.all()
    courses = models.Course.objects.all()
    meetings = models.Meeting.objects.all()
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        models.Info.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        print(request.POST)
    context = {
        'info':info,
        'best':best,
        'courses':courses,
        'meetings':meetings
    }
    return render(request,'index.html',context)
