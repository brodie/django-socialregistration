from django.conf import settings
from django.conf.urls import url, include
from socialregistration.views import Logout, Setup

urlpatterns = []

if 'socialregistration.contrib.openid' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^openid/', include('socialregistration.contrib.openid.urls',
            namespace='openid'))
    )

if 'socialregistration.contrib.twitter' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^twitter/', include('socialregistration.contrib.twitter.urls',
            namespace='twitter'))
    )

if 'socialregistration.contrib.linkedin' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^linkedin/', include('socialregistration.contrib.linkedin.urls',
            namespace='linkedin'))
    )

if 'socialregistration.contrib.facebook' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^facebook/', include('socialregistration.contrib.facebook.urls',
            namespace='facebook'))
    )

if 'socialregistration.contrib.github' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^github/', include('socialregistration.contrib.github.urls',
            namespace='github'))
    )

if 'socialregistration.contrib.foursquare' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^foursquare/', include('socialregistration.contrib.foursquare.urls',
            namespace='foursquare'))
    )

if 'socialregistration.contrib.tumblr' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^tumblr/', include('socialregistration.contrib.tumblr.urls',
            namespace='tumblr'))
    )

if 'socialregistration.contrib.instagram' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^instagram/', include('socialregistration.contrib.instagram.urls',
            namespace='instagram'))
    )

if 'socialregistration.contrib.google' in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r'^google/', include('socialregistration.contrib.google.urls',
            namespace='google'))
    )

urlpatterns.append(url(r'^setup/$', Setup.as_view(), name='setup'))
urlpatterns.append(url(r'^logout/$', Logout.as_view(), name='logout'))

