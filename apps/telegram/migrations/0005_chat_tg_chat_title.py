# Generated by Django 2.2.6 on 2019-11-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0004_chat_tg_chat_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='tg_chat_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title чата'),
        ),
    ]
