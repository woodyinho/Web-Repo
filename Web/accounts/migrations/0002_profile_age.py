# Generated by Django 2.2.7 on 2019-11-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]