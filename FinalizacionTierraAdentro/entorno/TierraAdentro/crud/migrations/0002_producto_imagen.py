# Generated by Django 4.0.1 on 2022-06-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='producto'),
        ),
    ]
