# Generated by Django 3.1.7 on 2021-04-23 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildSightApp', '0017_raw_sighting_new_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_sighting',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wildSightApp.species'),
        ),
    ]