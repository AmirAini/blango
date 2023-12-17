# Generated by Django 3.2.23 on 2023-12-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20231203_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
