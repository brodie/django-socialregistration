# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import socialregistration.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramAccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InstagramProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram', models.CharField(max_length=255)),
                ('site', models.ForeignKey(default=socialregistration.models.get_default_site, to='sites.Site')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instagramaccesstoken',
            name='profile',
            field=models.OneToOneField(related_name='access_token', to='instagram.InstagramProfile'),
            preserve_default=True,
        ),
    ]
