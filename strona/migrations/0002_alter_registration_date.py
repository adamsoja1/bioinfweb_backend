# Generated by Django 4.0 on 2022-08-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
