# Generated by Django 4.1.3 on 2023-01-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parents',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
