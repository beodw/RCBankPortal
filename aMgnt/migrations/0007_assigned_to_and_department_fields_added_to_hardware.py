# Generated by Django 3.1.4 on 2021-01-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aMgnt', '0006_department_table_and_supplied_department_tables_removed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(default='', max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='hardware',
            name='assigned_to',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hardware',
            name='department',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]