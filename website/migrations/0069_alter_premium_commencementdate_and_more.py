# Generated by Django 5.0.3 on 2024-09-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0068_alter_premium_dateofcancelorexpiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premium',
            name='commencementdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='premium',
            name='dateofcancelorexpiry',
            field=models.DateField(),
        ),
    ]
