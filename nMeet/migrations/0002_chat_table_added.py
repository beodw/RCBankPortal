# Generated by Django 3.1.4 on 2021-01-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nMeet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
                ('time_stamp', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='branch',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='credit',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='debit',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='teller_or_operator',
            field=models.CharField(max_length=15),
        ),
    ]
