# Generated by Django 5.0.1 on 2024-03-14 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customkit', '0011_alter_customorder_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customorder',
            name='order_number',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]