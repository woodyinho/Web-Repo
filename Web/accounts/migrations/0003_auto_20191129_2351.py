# Generated by Django 2.2.7 on 2019-11-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
