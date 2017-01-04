from socialregistration.compat.urls import url
from socialregistration.contrib.instagram.views import InstagramRedirect, \
    InstagramCallback, InstagramSetup

urlpatterns = [
    url('^redirect/$', InstagramRedirect.as_view(), name='redirect'),
    url('^callback/$', InstagramCallback.as_view(), name='callback'),
    url('^setup/$', InstagramSetup.as_view(), name='setup'),
]
