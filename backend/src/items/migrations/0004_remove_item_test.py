# Generated by Django 3.0.4 on 2020-03-08 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='test',
        ),
    ]