# Generated by Django 5.0.3 on 2024-09-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0065_premium_typeofcover'),
    ]

    operations = [
        migrations.AddField(
            model_name='premium',
            name='annualpremium',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='premium',
            name='refundstatus',
            field=models.CharField(blank=True, choices=[('refunded', 'Refund Made'), ('norefund', 'No Refund')], max_length=100, null=True),
        ),
    ]
