# Generated by Django 3.2.13 on 2022-07-07 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traininglog', '0015_alter_log1_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log2',
            name='time4',
        ),
        migrations.RemoveField(
            model_name='log2',
            name='time5',
        ),
        migrations.RemoveField(
            model_name='log2',
            name='time6',
        ),
        migrations.RemoveField(
            model_name='log2',
            name='time7',
        ),
        migrations.RemoveField(
            model_name='log2',
            name='time8',
        ),
    ]
