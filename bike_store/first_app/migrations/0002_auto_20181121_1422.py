# Generated by Django 2.1.3 on 2018-11-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_Type',
            new_name='vehicle_type',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
