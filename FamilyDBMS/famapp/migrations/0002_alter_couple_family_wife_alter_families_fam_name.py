# Generated by Django 4.1.3 on 2022-12-24 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couple_family',
            name='Wife',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='families',
            name='Fam_Name',
            field=models.CharField(max_length=50),
        ),
    ]
