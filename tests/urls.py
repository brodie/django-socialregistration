from socialregistration.compat.urls import *
from django.contrib import admin
from tests.app.views import index


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('socialregistration.urls', namespace='socialregistration')),
    url(r'^$', index, name='index'),
]
