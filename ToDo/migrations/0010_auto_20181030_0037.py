# Generated by Django 2.1.2 on 2018-10-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0009_todo_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='attachment',
            field=models.FileField(upload_to=''),
        ),
    ]