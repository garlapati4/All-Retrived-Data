from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(name__in=['Dhoni'])
    LWO=Webpage.objects.filter(name__in=['Sindhu','Nikki'])
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Q(name='Eeshu') | Q(url__startswith='https'))
    LWO=Webpage.objects.filter(Q(name='Nikki') & Q(url__startswith='http'))
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)
def display_access(request):
    LAO=AccessRecord.objects.all()
    LAO=AccessRecord.objects.filter(date__gt='2016-08-18')
    LAO=AccessRecord.objects.filter(date__lt='2016-08-18')
    LAO=AccessRecord.objects.filter(date__gte='2013-10-13')
    LAO=AccessRecord.objects.filter(date__lte='2013-10-13')
    LAO=AccessRecord.objects.all()
    LAO=AccessRecord.objects.filter(date__month='10')
    LAO=AccessRecord.objects.filter(date__year='2016')
    LAO=AccessRecord.objects.filter(date__year__gt='2014')
    d={'LAO':LAO}
    return render(request,'display_access.html',d)