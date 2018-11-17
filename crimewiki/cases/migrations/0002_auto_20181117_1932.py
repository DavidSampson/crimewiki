# Generated by Django 2.1.3 on 2018-11-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='files',
            field=models.ManyToManyField(blank=True, to='files.File'),
        ),
    ]
