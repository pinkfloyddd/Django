# Generated by Django 2.0.4 on 2018-04-28 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qidian', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qidian_xiaoshuo',
            old_name='nvoel_sub_type',
            new_name='novel_sub_type',
        ),
    ]
