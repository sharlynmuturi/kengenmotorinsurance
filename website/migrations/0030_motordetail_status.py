# Generated by Django 5.0.3 on 2024-09-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_privatemotor'),
    ]

    operations = [
        migrations.AddField(
            model_name='motordetail',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
