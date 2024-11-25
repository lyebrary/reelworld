# Generated by Django 5.1.3 on 2024-11-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_film_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='status',
            field=models.CharField(choices=[('REWATCHED', 'REWATCHED'), ('TO WATCH', 'TO WATCH'), ('WATCHED', 'WATCHED'), ('WATCHING', 'WATCHING')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]