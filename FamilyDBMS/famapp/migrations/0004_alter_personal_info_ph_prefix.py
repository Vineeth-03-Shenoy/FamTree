# Generated by Django 4.1.3 on 2022-12-31 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famapp', '0003_alter_personal_info_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='Ph_prefix',
            field=models.CharField(max_length=6),
        ),
    ]
