# Generated by Django 2.2.6 on 2019-11-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default=None, null=True, verbose_name='Текст записки')),
                ('access_token', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Токен доступа')),
                ('is_viewed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Просмотрено')),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'записка',
                'verbose_name_plural': 'записки',
            },
        ),
    ]
