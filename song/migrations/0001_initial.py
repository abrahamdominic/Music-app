# Generated by Django 4.1.2 on 2022-10-07 22:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artiste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_released', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('likes', models.IntegerField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artiste.artiste')),
            ],
        ),
    ]