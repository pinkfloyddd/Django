from django.shortcuts import render

from . import models
def index(request):
    novel_info_table = models.Qidian_Xiaoshuo.objects.all()
    chapter_detail_table = models.Chapter_Detail_Table.objects.all()
    return render(request,'index.html',{'novel_info_table':novel_info_table,'chapter_detail_table':chapter_detail_table})
def qidian_contain(request):
    chapter_detail_table = models.Chapter_Detail_Table.object.all()
    return  render(request,'qidian_contain.html',{'chapter_detail_table':chapter_detail_table})