# Generated by Django 3.1.1 on 2021-04-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_experience_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='enddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='startdate',
            field=models.DateField(),
        ),
    ]