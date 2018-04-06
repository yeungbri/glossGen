from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect
import datetime
import os
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from glossGen.settings import PROJECT_ROOT
from glossGen.forms import UploadFileForm
from .keywordExtraction.GGkeyphrase import GGkeyphrase
import wikipedia
from .GG import GGmain

result = [[("keyphrase","defintion"), ("keyphrase","defintion")], [("keyphrase","defintion")]]

def gloss(request):
    return render(request, 'gloss.html', {'result':result})

def upload(request):
    return render(request, 'upload.html')

def handleUploadedFile(f):
    global result
    with open('target.txt', 'wb+') as dst:
        for chunk in f.chunks():
            dst.write(chunk)
            #print(chunk)
    #keywords = GGkeyphrase()
    result = GGmain()
    #result = [[("keyphrase","defintion"), ("keyphrase","defintion")], [("keyphrase","defintion")]]

def uploadTarget(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            result = handleUploadedFile(request.FILES['file'])
            return render(request, 'gloss.html')
    return render('error.html', {'error': "Couldn't Upload File"})

def error(request):
    return render(request, 'error.html')

def test(request):
    return render(request, 'test.html')