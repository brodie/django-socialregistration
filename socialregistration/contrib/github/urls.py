from socialregistration.compat.urls import url
from socialregistration.contrib.github.views import GithubRedirect, \
    GithubCallback, GithubSetup

urlpatterns = [
    url('^redirect/$', GithubRedirect.as_view(), name='redirect'),
    url('^callback/$', GithubCallback.as_view(), name='callback'),
    url('^setup/$', GithubSetup.as_view(), name='setup'),
]
