# Generated by Django 4.0.5 on 2022-06-09 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='last_name',
        ),
        migrations.AlterModelTable(
            name='employerprofile',
            table='employerprofile',
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'EmployeeProfile',
                'verbose_name_plural': 'EmployeeProfile',
                'db_table': 'employeeprofile',
                'managed': True,
            },
        ),
    ]