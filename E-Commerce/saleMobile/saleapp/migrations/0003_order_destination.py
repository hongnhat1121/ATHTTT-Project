# Generated by Django 4.0.3 on 2022-03-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleapp', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='destination',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
