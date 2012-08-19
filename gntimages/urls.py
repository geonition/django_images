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
            #svg images
            url(r'^svg/place_marker.svg',
                'place_marker',
                name='place_marker'),
            url(r'^svg/route_marker.svg',
                'route_marker',
                name='route_marker'),
            url(r'^svg/area_marker.svg',
                'area_marker',
                name='area_marker'),
        )
