# Generated by Django 4.0.3 on 2022-03-18 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saleapp', '0004_alter_order_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', related_query_name='my_product', to='saleapp.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='products/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, upload_to='user/%Y/%m'),
        ),
    ]
