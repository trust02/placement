# Generated by Django 5.0.1 on 2024-05-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='attachment_status',
            field=models.CharField(null=True),
        ),
    ]
