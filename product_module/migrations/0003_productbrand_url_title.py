# Generated by Django 4.0.10 on 2023-07-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='url_title', max_length=300, verbose_name='نام در url'),
            preserve_default=False,
        ),
    ]