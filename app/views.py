from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *


def form_display(request):
    TFO=TopicForm()
    WFO=WebpageForm()
    ARFO=AccessRecordForm()
    d={'TFO':TFO,'WFO':WFO,'ARFO':ARFO}
    if request.method=='POST' and request.FILES:
        TFD=TopicForm(request.POST)
        WFD=WebpageForm(request.POST,request.FILES)
        ARFD=AccessRecordForm(request.POST,request.FILES)
        if TFD.is_valid() and WFD.is_valid() and ARFD.is_valid():
           TO=TFD.save(commit=False)
           TO.save()
           WO=WFD.save(commit=False)
           WO.topic_name=TO
           WO.save()
           AO=ARFD.save(commit=False)
           AO.name=WO
           AO.save()
           return HttpResponse('registritation is successfully done ')
    return render(request,'form_display.html',d)
