# Generated by Django 3.2.9 on 2022-12-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0009_alter_job_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
