# Generated by Django 3.1.4 on 2021-01-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aMgnt', '0007_assigned_to_and_department_fields_added_to_hardware'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='assigned_to',
            field=models.CharField(blank=True, default='Not yet assigned', max_length=100),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='department',
            field=models.CharField(blank=True, default='Not yet assigned', max_length=100),
        ),
    ]
