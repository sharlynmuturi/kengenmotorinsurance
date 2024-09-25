# Generated by Django 4.2.16 on 2024-09-22 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=100, unique=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('sumassured', models.IntegerField(null=True)),
                ('make', models.CharField(max_length=100, null=True)),
                ('rating', models.CharField(max_length=100, null=True)),
                ('chasisno', models.CharField(max_length=100, null=True)),
                ('yom', models.IntegerField(null=True)),
                ('commencementdate', models.DateField(default=datetime.date.today, null=True)),
                ('logbook', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(blank=True, choices=[('absent', 'Cover Not Provided'), ('active', 'Cover Active'), ('cancelled', 'Cover Cancelled')], default='absent', max_length=100, null=True)),
                ('dateofcancelorexpiry', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('staffno', models.IntegerField(blank=True, null=True)),
                ('typeofcover', models.CharField(choices=[('comprehensive', 'Comprehensive'), ('thirdparty', 'ThirdParty')], max_length=100, null=True)),
                ('commencementdate', models.DateField(default=datetime.date.today)),
                ('dateofcancelorexpiry', models.DateField(default=datetime.date.today)),
                ('sumassured', models.IntegerField()),
                ('premiumrate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('annualpremium', models.IntegerField(blank=True, default=0)),
                ('prorata', models.IntegerField(blank=True, default=0)),
                ('windscreenadditionalpremium', models.IntegerField(default=0)),
                ('radioadditionalpremium', models.IntegerField(default=0)),
                ('courtesycar', models.IntegerField(default=0)),
                ('excessprotector', models.IntegerField(default=0)),
                ('grandtotal', models.IntegerField(blank=True, default=0, null=True)),
                ('levies', models.IntegerField(blank=True, default=0, null=True)),
                ('premiumpayable', models.IntegerField(blank=True, default=0, null=True)),
                ('amountpaid', models.IntegerField(blank=True, default=0, null=True)),
                ('amountremaining', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(blank=True, choices=[('paid', 'Payment Made'), ('partpaid', 'Part Payment'), ('unpaid', 'Payment Not Made')], max_length=100, null=True)),
                ('paymentmethod', models.CharField(blank=True, choices=[('cashpayment', 'Cash Payment'), ('salarydeduction', 'Salary Deduction'), ('otherpayment', 'Other')], max_length=100, null=True)),
                ('amountrefund', models.IntegerField(blank=True, default=0, null=True)),
                ('refundstatus', models.CharField(blank=True, choices=[('refunded', 'Refund Made'), ('norefund', 'No Refund')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=100, unique=True)),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('staffno', models.IntegerField(null=True)),
                ('employmentstatus', models.CharField(choices=[('staff', 'Staff'), ('director/manager', 'Director/Manager'), ('ex-staff', 'Ex-Staff'), ('ex-director/manager', 'Ex-Director/Manager')], max_length=100, null=True)),
                ('email', models.EmailField(default='example@example.com', max_length=254, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('phoneno', models.CharField(max_length=15, null=True)),
                ('idno', models.IntegerField(null=True)),
                ('krapin', models.CharField(max_length=100, null=True)),
                ('sumassured', models.CharField(max_length=100, null=True)),
                ('make', models.CharField(max_length=100, null=True)),
                ('rating', models.CharField(max_length=100, null=True)),
                ('chasisno', models.CharField(max_length=100, null=True)),
                ('yom', models.IntegerField(null=True)),
                ('typeofvehicle', models.CharField(choices=[('private', 'Private'), ('commercial', 'Commercial')], max_length=100, null=True)),
                ('typeofcover', models.CharField(choices=[('comprehensive', 'Comprehensive'), ('thirdparty', 'ThirdParty')], max_length=100, null=True)),
                ('commencementdate', models.DateField(default=datetime.date.today, null=True)),
                ('logbook', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(blank=True, choices=[('absent', 'Cover Not Provided'), ('active', 'Cover Active'), ('cancelled', 'Cover Cancelled')], default='absent', max_length=100, null=True)),
                ('dateofcancelorexpiry', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
