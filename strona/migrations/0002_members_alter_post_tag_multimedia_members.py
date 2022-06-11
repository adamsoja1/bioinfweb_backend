# Generated by Django 4.0 on 2022-05-20 23:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('position', models.CharField(max_length=150)),
                ('about', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='strona.Tags'),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='members',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='strona.members'),
            preserve_default=False,
        ),
    ]