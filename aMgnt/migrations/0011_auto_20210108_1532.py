# Generated by Django 3.1.4 on 2021-01-08 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aMgnt', '0010_All_system_unit_serial_number_components_optional_for_initial_integration_of_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='date_of_supply',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='serial_number',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
    ]
