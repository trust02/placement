# Generated by Django 5.0.1 on 2024-04-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_attachmentpost_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='companysignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(null=True)),
                ('company_category', models.CharField(null=True)),
                ('username', models.CharField(null=True)),
                ('email', models.CharField(null=True)),
                ('password', models.CharField(null=True)),
            ],
        ),
    ]
