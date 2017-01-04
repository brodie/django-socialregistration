from socialregistration.compat.urls import url
from socialregistration.contrib.linkedin.views import LinkedInRedirect, \
    LinkedInCallback, LinkedInSetup

urlpatterns = [
    url('^redirect/$', LinkedInRedirect.as_view(), name='redirect'),
    url('^callback/$', LinkedInCallback.as_view(), name='callback'),
    url('^setup/$', LinkedInSetup.as_view(), name='setup'),
]
