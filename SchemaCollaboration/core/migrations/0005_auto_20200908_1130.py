# Generated by Django 3.1.1 on 2020-09-08 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_add_comments_todos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='done_by',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='ToDo',
        ),
    ]
