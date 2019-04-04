# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtailmenus.models import MenuPage


class TutorialsHomePage(MenuPage):
    sub_title = models.CharField(max_length=250, null=True, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        FieldPanel('body', classname="full"),
    ]
