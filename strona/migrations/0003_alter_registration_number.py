# Generated by Django 4.0 on 2022-08-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0002_alter_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='number',
            field=models.CharField(max_length=12),
        ),
    ]
