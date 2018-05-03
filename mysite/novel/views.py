from django.shortcuts import render
# from django.http import HttpResponse
# from django.db import models
from . import models
def index(request):
    return render(request,'novel/index.html',{'test1':'this is test key'})
def novel_info(request):
    novel_info_tables = models.novel_info.objects.all()
    return render(request,'novel/novel_info.html',{'novelinfos':novel_info_tables})
