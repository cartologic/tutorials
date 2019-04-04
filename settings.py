TUTORIALS_APPS = (
        'wagtail.wagtailforms',
        'wagtail.wagtailredirects',
        'wagtail.wagtailembeds',
        'wagtail.wagtailsites',
        'wagtail.wagtailusers',
        'wagtail.wagtailsnippets',
        'wagtail.wagtaildocs',
        'wagtail.wagtailimages',
        'wagtail.wagtailsearch',
        'wagtail.wagtailadmin',
        'wagtail.wagtailcore',
        'modelcluster',
         'wagtail.contrib.modeladmin',
        'taggit',
        'wagtailmenus',
)
TUTORIALS_MIDDLEWARE = (
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)
TUTORIALS_PROCESSORS = (
    'wagtail.contrib.settings.context_processors.settings',
    'wagtailmenus.context_processors.wagtailmenus',
)
for app_name in TUTORIALS_APPS:
    if app_name not in INSTALLED_APPS:
        INSTALLED_APPS += (app_name,)
for app_middle in TUTORIALS_MIDDLEWARE:
    if app_middle not in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES += (app_middle,)

WAGTAIL_SITE_NAME = "Cartoview"
CURRENT_PROCESSORS = TEMPLATES[0]['OPTIONS']['context_processors']
for p in TUTORIALS_PROCESSORS:
    if p not in CURRENT_PROCESSORS:
        CURRENT_PROCESSORS += [p, ]
TEMPLATES[0]['OPTIONS']['context_processors'] = CURRENT_PROCESSORS
