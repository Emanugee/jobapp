# Generated by Django 4.0.5 on 2022-06-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0011_alter_listjob_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='listjob',
            name='display',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
