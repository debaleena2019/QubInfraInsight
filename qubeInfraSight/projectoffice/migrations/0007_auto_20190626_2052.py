# Generated by Django 2.2.1 on 2019-06-26 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectoffice', '0006_auto_20190625_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='customeradditionalattribute',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='customerlegalinfo',
            options={'managed': True},
        ),
    ]
