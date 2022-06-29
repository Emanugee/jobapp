# Generated by Django 4.0.5 on 2022-06-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_alter_employeeprofile_phone'),
        ('postjob', '0009_alter_listjob_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listjob',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.employerprofile'),
        ),
        migrations.AlterField(
            model_name='listjob',
            name='logo',
            field=models.ImageField(default='logo/i.jpg', upload_to='logo'),
        ),
    ]