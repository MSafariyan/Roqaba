# Generated by Django 3.2 on 2021-09-07 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_book_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='ref',
            field=models.URLField(max_length=555, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
