# Generated by Django 3.1.1 on 2021-02-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210202_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userImage',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]
