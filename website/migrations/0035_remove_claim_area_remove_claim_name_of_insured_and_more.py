# Generated by Django 5.0.3 on 2024-09-10 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_remove_staffmember_staff_motor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim',
            name='AREA',
        ),
        migrations.RemoveField(
            model_name='claim',
            name='NAME_OF_INSURED',
        ),
        migrations.RemoveField(
            model_name='claim',
            name='REG_NUMBER',
        ),
        migrations.RemoveField(
            model_name='claim',
            name='STAFF_NUMBER',
        ),
        migrations.AddField(
            model_name='claim',
            name='VEHICLE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.motordetail', to_field='regno', unique=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='REMARKS',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='motordetail',
            name='regno',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
