from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('gntimages.views',
            url(r'^needle',
                'needle',
                name='image_needle'),
            url(r'^route',
                'route',
                name='image_route'),
            url(r'^area',
                'area',
                name='image_area'),
        )
