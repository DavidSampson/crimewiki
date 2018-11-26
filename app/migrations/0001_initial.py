# Generated by Django 2.1.3 on 2018-11-26 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Page')),
                ('content', models.TextField()),
            ],
            bases=('app.page',),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Page')),
                ('type', models.CharField(blank=True, choices=[('image', 'image'), ('video', 'video'), ('pdf', 'pdf'), ('audio', 'audio'), ('other', 'other')], max_length=10)),
                ('source', models.CharField(blank=True, max_length=200)),
                ('file_path', models.FileField(upload_to='')),
            ],
            bases=('app.page',),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Page')),
                ('place', models.CharField(max_length=200)),
            ],
            bases=('app.page',),
        ),
        migrations.AddField(
            model_name='page',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
