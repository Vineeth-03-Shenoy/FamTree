# Generated by Django 4.1.3 on 2022-12-08 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('famapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parents',
            name='child_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='famapp.family_member'),
        ),
    ]