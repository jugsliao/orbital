# Generated by Django 3.2.13 on 2022-06-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traininglog', '0013_alter_log1_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log1',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
