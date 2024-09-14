# Generated by Django 5.0.3 on 2024-03-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_staff_idno_alter_staff_krapin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='motordetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('staffno', models.IntegerField()),
                ('area', models.CharField(max_length=100)),
                ('phoneno', models.IntegerField()),
                ('idno', models.IntegerField()),
                ('krapin', models.IntegerField()),
                ('commencementdate', models.DateField()),
                ('expirydate', models.DateField()),
                ('sumassured', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='staff',
        ),
    ]
