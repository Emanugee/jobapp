# Generated by Django 4.0.5 on 2022-06-11 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_rename_company_name_employerprofile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='gender',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
