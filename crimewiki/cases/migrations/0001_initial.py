# Generated by Django 2.1.3 on 2018-11-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0003_auto_20181116_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('files', models.ManyToManyField(to='files.File')),
            ],
        ),
    ]