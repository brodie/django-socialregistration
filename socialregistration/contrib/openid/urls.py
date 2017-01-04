from socialregistration.compat.urls import url
from socialregistration.contrib.openid.views import OpenIDRedirect, \
    OpenIDCallback, OpenIDSetup

urlpatterns = [
    url('^redirect/$', OpenIDRedirect.as_view(), name='redirect'),
    url('^callback/$', OpenIDCallback.as_view(), name='callback'),
    url('^setup/$', OpenIDSetup.as_view(), name='setup'),
]
