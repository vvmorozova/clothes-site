# Generated by Django 4.1.7 on 2023-03-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0006_item_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=1000),
        ),
    ]
