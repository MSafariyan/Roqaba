# Generated by Django 3.2 on 2021-08-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_book_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(help_text='link of image', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(help_text='link of image', max_length=255, null=True),
        ),
    ]