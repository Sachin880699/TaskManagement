# Generated by Django 3.2.23 on 2023-12-22 02:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2023, 12, 22, 2, 56, 21, 988263, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
