# Generated by Django 3.2.9 on 2022-12-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0007_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
