# Generated by Django 2.2.7 on 2019-11-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecampus', '0013_auto_20191126_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='conteudo',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='sutia',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
