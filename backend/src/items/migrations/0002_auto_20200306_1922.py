# Generated by Django 3.0.4 on 2020-03-06 18:22

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='hideout',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quests',
        ),
        migrations.AlterField(
            model_name='item',
            name='img_info',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='notes',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]