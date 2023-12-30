# Generated by Django 3.2.23 on 2023-12-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20231221_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employeeuser',
            name='employee_status',
        ),
        migrations.AlterField(
            model_name='employeeuser',
            name='experty',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Experty'),
        ),
        migrations.RemoveField(
            model_name='employeeuser',
            name='role',
        ),
        migrations.AddField(
            model_name='employeeuser',
            name='employee_status',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.EmployeeStatus'),
        ),
        migrations.AddField(
            model_name='employeeuser',
            name='role',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.EmployeeRole'),
        ),
    ]