# Generated by Django 3.2.23 on 2023-12-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20231221_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]