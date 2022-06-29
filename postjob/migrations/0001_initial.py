# Generated by Django 4.0.5 on 2022-06-14 13:07

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Listjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=100)),
                ('job_type', models.CharField(default='a', max_length=50)),
                ('description', models.TextField()),
                ('tags', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=50)),
                ('deadline', models.DateField()),
                ('logo', models.ImageField(upload_to='logo')),
                ('website', models.URLField(blank=True, null=True)),
                ('posted_at', models.DateField(auto_now=True)),
                ('published', models.BooleanField()),
                ('closed', models.BooleanField()),
                ('featured', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postjob.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Listjob',
                'verbose_name_plural': 'Listjob',
                'db_table': 'listjob',
                'managed': True,
            },
        ),
    ]