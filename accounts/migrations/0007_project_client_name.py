# Generated by Django 3.2.23 on 2023-12-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20231221_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='client_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
