# Generated by Django 2.2 on 2020-10-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
