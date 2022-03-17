# Generated by Django 4.0.3 on 2022-03-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleapp', '0004_alter_order_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Products/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='Avatars/%Y/%m'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'category')},
        ),
    ]