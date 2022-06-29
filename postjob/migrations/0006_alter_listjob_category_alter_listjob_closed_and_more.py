# Generated by Django 4.0.5 on 2022-06-20 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postjob', '0005_remove_listjob_catgory_listjob_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listjob',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postjob.category'),
        ),
        migrations.AlterField(
            model_name='listjob',
            name='closed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listjob',
            name='featured',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listjob',
            name='published',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
