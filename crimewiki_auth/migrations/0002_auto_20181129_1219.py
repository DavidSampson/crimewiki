# Generated by Django 2.1.3 on 2018-11-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimewiki_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionstrategy',
            name='action',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='permissionstrategy',
            name='role',
            field=models.CharField(max_length=200),
        ),
    ]
