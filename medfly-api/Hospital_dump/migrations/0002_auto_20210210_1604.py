# Generated by Django 3.1.5 on 2021-02-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='Owner_Password',
            field=models.CharField(default='MedFly_Name', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Account_Type',
            field=models.CharField(default='Demo', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Owner_Username',
            field=models.CharField(default='Mobile', max_length=20),
        ),
    ]