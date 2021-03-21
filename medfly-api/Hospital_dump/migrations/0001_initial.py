# Generated by Django 3.0.7 on 2020-12-18 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosp_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Department_Name', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosp_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Device_Id', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosp_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('Mobile', models.PositiveIntegerField()),
                ('Location', models.CharField(max_length=100)),
                ('Having_Branch', models.BooleanField(default=False)),
                ('Branch_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Branch_Type', models.CharField(default='Main', max_length=100)),
                ('Owner_Name', models.CharField(max_length=100)),
                ('Logo', models.CharField(blank=True, max_length=50, null=True)),
                ('Account_Type', models.CharField(default='Licensed', max_length=20)),
                ('Account_StartDate', models.DateField(default=datetime.datetime.now)),
                ('Account_ExpiryDate', models.DateField(blank=True, null=True)),
                ('Installation_Date', models.CharField(blank=True, max_length=20, null=True)),
                ('Admin_Username', models.CharField(blank=True, max_length=20, null=True)),
                ('Owner_Username', models.CharField(blank=True, max_length=20, null=True)),
                ('Quoted', models.CharField(blank=True, max_length=20, null=True)),
                ('Finalised_Cost', models.CharField(blank=True, max_length=20, null=True)),
                ('Payment_Mode', models.CharField(blank=True, max_length=20, null=True)),
                ('Due', models.CharField(blank=True, max_length=20, null=True)),
                ('Paid_By', models.CharField(blank=True, max_length=20, null=True)),
                ('Lead_by', models.CharField(blank=True, max_length=20, null=True)),
                ('Contact_Person', models.CharField(blank=True, max_length=20, null=True)),
                ('Payment_Process', models.CharField(blank=True, max_length=20, null=True)),
                ('Total_Devices', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hsp_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('Mf_Id', models.CharField(max_length=100)),
                ('Procedure_Name', models.CharField(max_length=100)),
                ('File_Src', models.CharField(max_length=100)),
                ('File_Thumbnail', models.CharField(max_length=100)),
                ('File_Type', models.CharField(default='snap', max_length=10)),
                ('File_Status', models.CharField(default='main', max_length=10)),
                ('Annotation_Data', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hsp_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('Menu_Name', models.CharField(max_length=100)),
                ('Menu_Path', models.CharField(max_length=100)),
                ('Menu_Icon', models.CharField(max_length=100)),
                ('Menu_Status', models.CharField(default='Active', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hsp_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('Mf_Id', models.CharField(max_length=100)),
                ('Patient_Name', models.CharField(max_length=100)),
                ('Mobile', models.PositiveIntegerField()),
                ('Age', models.PositiveIntegerField()),
                ('Gender', models.CharField(max_length=100)),
                ('Alt_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.CharField(max_length=100)),
                ('Total_Visits', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hsp_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('Mf_Id', models.CharField(max_length=100)),
                ('Alt_Id', models.CharField(max_length=100)),
                ('Procedure_Id', models.PositiveIntegerField()),
                ('Procedure_Name', models.CharField(max_length=100)),
                ('Doctor_Id', models.PositiveIntegerField()),
                ('Doctor_Name', models.CharField(max_length=100)),
                ('Anesthesian_Name', models.CharField(max_length=100)),
                ('Referrer_Name', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosp_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Department_ID', models.PositiveIntegerField()),
                ('Department_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Procedure_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Procedure_Status', models.CharField(default='Active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosp_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Report_Name', models.CharField(max_length=100)),
                ('Department_ID', models.PositiveIntegerField()),
                ('Department_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Procedure_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Template_ID', models.PositiveIntegerField()),
                ('Template_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Parameter_Name', models.CharField(max_length=50)),
                ('Parameter_Value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosp_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Role_ID', models.PositiveIntegerField()),
                ('Role_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Department_ID', models.PositiveIntegerField()),
                ('Department_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Permissions', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hosp_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Department_ID', models.PositiveIntegerField()),
                ('Department_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Procedure_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Template_Name', models.CharField(blank=True, max_length=120, null=True)),
                ('Template_Status', models.CharField(default='Create', max_length=20)),
            ],
        ),
    ]
