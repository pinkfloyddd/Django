from django.db import models

class Qidian_Xiaoshuo(models.Model):
    novel_name = models.CharField(max_length = 100,primary_key = True)
    novel_writter = models.CharField(max_length = 100)
    novel_main_type = models.CharField(max_length = 100)
    novel_sub_type = models.CharField(max_length = 100)
    novel_status = models.CharField(max_length = 100)
    novel_img_url = models.URLField()
    novel_real_url = models.URLField()
    novel_update_time = models.DateTimeField(auto_now = True)

class Chapter_Detail_Table(models.Model):
    novel_name = models.CharField(max_length = 100)
    novel_chapter_name = models.CharField(max_length = 100)
    novel_chapter_id = models.IntegerField(primary_key = True,auto_created = True)
    novel_chapter_url = models.CharField(max_length = 100)
    novel_chapter_context = models.TextField()
    chapter_update_time = models.DateTimeField(auto_now = True)




