# Generated by Django 5.0.3 on 2024-09-09 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_motordetail_canceldate_motordetail_chasisno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motordetail',
            name='yom',
        ),
    ]
