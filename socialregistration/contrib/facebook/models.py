from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from django.db import models
from socialregistration.models import get_default_site
from socialregistration.signals import connect, login

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class FacebookProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL)
    site = models.ForeignKey(Site, default=get_default_site)
    uid = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        try:
            return u'%s: %s' % (self.user, self.uid)
        except models.ObjectDoesNotExist:
            return u'None'

    def authenticate(self):
        return authenticate(uid=self.uid)

class FacebookAccessToken(models.Model):
    profile = models.OneToOneField(FacebookProfile, related_name='access_token')
    access_token = models.CharField(max_length=255)


def save_facebook_token(sender, user, profile, client, **kwargs):
    try:
        FacebookAccessToken.objects.get(profile=profile).delete()
    except FacebookAccessToken.DoesNotExist:
        pass

    FacebookAccessToken.objects.create(profile=profile,
        access_token=client.graph.access_token)

connect.connect(save_facebook_token, sender=FacebookProfile,
    dispatch_uid='socialregistration.facebook.connect')
login.connect(save_facebook_token, sender = FacebookProfile,
    dispatch_uid = 'socialregistration.facebook.login')
