# Generated by Django 2.1.3 on 2018-11-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FilePathField(verbose_name='C:\\Users\\wm6sek\\Code\\crime-wiki\\crimewiki\\uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('files', models.ManyToManyField(to='files.File')),
            ],
        ),
    ]