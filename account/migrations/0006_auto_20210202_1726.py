# Generated by Django 3.1.1 on 2021-02-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210202_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userImage',
            field=models.ImageField(blank=True, default='profile_pics/default.png', null=True, upload_to='profile_pics/'),
        ),
    ]
