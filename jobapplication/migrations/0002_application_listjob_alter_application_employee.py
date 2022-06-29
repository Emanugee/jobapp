# Generated by Django 4.0.5 on 2022-06-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0007_remove_listjob_user_listjob_employer'),
        ('userprofile', '0014_delete_move'),
        ('jobapplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='listjob',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='postjob.listjob'),
        ),
        migrations.AlterField(
            model_name='application',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.employeeprofile'),
        ),
    ]
