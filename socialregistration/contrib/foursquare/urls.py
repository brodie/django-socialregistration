from socialregistration.compat.urls import url
from socialregistration.contrib.foursquare.views import FoursquareRedirect, \
    FoursquareCallback, FoursquareSetup


urlpatterns = [
    url('^redirect/$', FoursquareRedirect.as_view(), name='redirect'),
    url('^callback/$', FoursquareCallback.as_view(), name='callback'),
    url('^setup/$', FoursquareSetup.as_view(), name='setup'),
]
