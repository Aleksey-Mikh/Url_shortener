# Generated by Django 3.2.9 on 2022-01-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('short_url', models.SlugField(max_length=7, primary_key=True, serialize=False)),
                ('origin_url', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
                'ordering': ['origin_url'],
            },
        ),
    ]