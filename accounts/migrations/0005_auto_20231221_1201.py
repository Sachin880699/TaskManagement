# Generated by Django 3.2.23 on 2023-12-21 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20231221_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeuser',
            name='employee_status',
        ),
        migrations.AddField(
            model_name='employeeuser',
            name='employee_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.employeestatus'),
        ),
    ]
