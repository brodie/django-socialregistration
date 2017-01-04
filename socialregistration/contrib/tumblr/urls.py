from socialregistration.compat.urls import url
from socialregistration.contrib.tumblr.views import TumblrRedirect, \
    TumblrCallback, TumblrSetup


urlpatterns = [
    url('^redirect/$', TumblrRedirect.as_view(), name='redirect'),
    url('^callback/$', TumblrCallback.as_view(), name='callback'),
    url('^setup/$', TumblrSetup.as_view(), name='setup'),
]
