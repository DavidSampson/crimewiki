# Generated by Django 2.1.3 on 2018-11-29 18:19

from django.db import migrations
from crimewiki_auth.models import PERMISSION_STRATEGIES


def add_permission_strategies(apps, schema_editor):
    PermissionStrategy = apps.get_model('crimewiki_auth', 'PermissionStrategy')
    for s in PERMISSION_STRATEGIES:
        PermissionStrategy.objects.create(**s)


class Migration(migrations.Migration):

    dependencies = [
        ('crimewiki_auth', '0003_permissionstrategy_description'),
    ]

    operations = [
        migrations.RunPython(add_permission_strategies)
    ]
