# Generated by Django 3.1 on 2021-02-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_auto_20210211_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='Department_ID',
            field=models.PositiveIntegerField(default=0),
        ),
    ]