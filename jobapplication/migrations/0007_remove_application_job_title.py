# Generated by Django 4.0.5 on 2022-06-22 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplication', '0006_alter_application_employer_alter_application_listjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='job_title',
        ),
    ]