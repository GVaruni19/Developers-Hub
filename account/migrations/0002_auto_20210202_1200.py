# Generated by Django 3.1.1 on 2021-02-02 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userImage',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics '),
        ),
    ]
