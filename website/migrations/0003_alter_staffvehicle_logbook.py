# Generated by Django 4.2.16 on 2024-09-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_staffmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffvehicle',
            name='logbook',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
