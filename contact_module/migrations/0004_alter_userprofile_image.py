# Generated by Django 4.2.2 on 2023-06-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
