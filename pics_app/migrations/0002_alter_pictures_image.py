# Generated by Django 4.2.8 on 2023-12-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(upload_to='uploaded_pics/'),
        ),
    ]