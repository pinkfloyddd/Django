# Generated by Django 2.0.4 on 2018-04-28 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qidian', '0002_auto_20180428_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qidian_xiaoshuo',
            name='novel_chapter_name',
        ),
        migrations.RemoveField(
            model_name='qidian_xiaoshuo',
            name='novel_chapter_save_path',
        ),
        migrations.RemoveField(
            model_name='qidian_xiaoshuo',
            name='novel_img_save_path',
        ),
    ]