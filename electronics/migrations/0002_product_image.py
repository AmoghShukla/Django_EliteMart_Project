# Generated by Django 5.1.6 on 2025-02-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='https://via.placeholder.com/150', upload_to='product_img/'),
        ),
    ]
