from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
import os
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from selfimprovement.settings import PROJECT_ROOT

def hello(request):
    return HttpResponse("Hello World")

def curDateTime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date':now})

def home(request):
    return HttpResponse("Home")
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    #html = "In %s hour(s), it will be %s." % (offset, dt)
    #return HttpResponse(html)
    return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':dt, })
        
def makeNote(request):
    if request.method == 'POST':
        name = '/notes/' + request.POST.get('filename')
        if os.path.isfile(name):
            return HttpResponse("Error: Filename in use")
        else:
            f = open(name,"w+")
            return HttpResponseRedirect('/notedir')

def notedir(request):
    return render(request, 'notedir.html', {'files':os.listdir('notes')})
    
def viewnote(request, filename):
    try:
        note = str(filename)
    except ValueError:
        raise Http404()
    return render(request, 'viewnote.html', {'note': note})

# time_log Page
def time_log(request):
    fp = open(os.path.join(PROJECT_ROOT, 'time_log'))
    timeLog = []
    for line in fp:
        timeLog.append(line)
    timeLog = reversed(timeLog)
    return render(request, 'time_log.html', {"time_log":timeLog})

def log_timelog(request):
    if request.method == 'POST':
        now = datetime.datetime.now()
        item = request.POST.get('item_field')
        with open(os.path.join(PROJECT_ROOT, 'time_log'), 'a') as f:
            item = str(now) + " " + item + "\n"
            f.write(item)
        return HttpResponseRedirect('/time_log/')