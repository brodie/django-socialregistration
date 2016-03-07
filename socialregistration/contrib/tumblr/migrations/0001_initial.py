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
            name='TumblrAccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oauth_token', models.CharField(max_length=80)),
                ('oauth_token_secret', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TumblrProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tumblr', models.CharField(max_length=100)),
                ('site', models.ForeignKey(default=socialregistration.models.get_default_site, to='sites.Site')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TumblrRequestToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oauth_token', models.CharField(max_length=80)),
                ('oauth_token_secret', models.CharField(max_length=80)),
                ('profile', models.OneToOneField(related_name='request_token', to='tumblr.TumblrProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tumblraccesstoken',
            name='profile',
            field=models.OneToOneField(related_name='access_token', to='tumblr.TumblrProfile'),
            preserve_default=True,
        ),
    ]
