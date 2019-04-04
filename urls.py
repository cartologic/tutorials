# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from . import APP_NAME

urlpatterns = [
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^', include(wagtail_urls), name="%s.index" % (APP_NAME)),
]
