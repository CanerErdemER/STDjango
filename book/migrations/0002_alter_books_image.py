# Generated by Django 5.1 on 2024-08-26 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, max_length=50, upload_to=''),
        ),
    ]
