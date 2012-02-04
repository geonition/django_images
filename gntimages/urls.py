from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('gntimages.views',
            #test templates
            url(r'^needle',
                'needle',
                name='image_needle'),
        )
