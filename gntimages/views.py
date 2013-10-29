from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.cache import patch_cache_control
import Image
import ImageChops
import os

def needle(request):
    color = request.GET.get('color', 'ffffff')
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)
    new_color = (red, green, blue)
    new_scale = float(request.GET.get('scale', '1.0'))

    #requires the images to be in MEDIA_ROOT
    base_img = Image.open('%s/%s' % (settings.MEDIA_ROOT,
                                    'base_needle.png'))
    color_img = Image.open('%s/%s' % (settings.MEDIA_ROOT,
                                    'needle_mask.png'))
    base_pixels = base_img.load()
    color_pixels = color_img.load()

    #change the color
    for y in xrange(color_img.size[1]):
        for x in xrange(color_img.size[0]):
            if color_pixels[x, y][0:3] == (255,0,0):
                new_color = (new_color[0], new_color[1], new_color[2], color_pixels[x, y][3])
                color_pixels[x,y] = new_color

    new_image = color_img.copy()
    new_img_data = new_image.load()
    for y in xrange(color_img.size[1]):
        for x in xrange(color_img.size[0]):
            new_red = color_pixels[x, y][0] * (color_pixels[x, y][3] / 255.0) * (1 - base_pixels[x, y][3] / 255.0) + base_pixels[x, y][0] * (base_pixels[x, y][3] / 255.0)
            new_green = color_pixels[x, y][1] * (color_pixels[x, y][3] / 255.0) * (1 - base_pixels[x, y][3] / 255.0) + base_pixels[x, y][1] * (base_pixels[x, y][3] / 255.0)
            new_blue = color_pixels[x, y][2] * (color_pixels[x, y][3] / 255.0) * (1 - base_pixels[x, y][3] / 255.0) + base_pixels[x, y][2] * (base_pixels[x, y][3] / 255.0)
            new_alpha = (color_pixels[x, y][3] + base_pixels[x, y][3])
            new_img_data[x, y] = (int(new_red), int(new_green), int(new_blue), int(new_alpha))

    new_image = new_image.resize((int(new_image.size[0] * new_scale), int(new_image.size[1] * new_scale)))

    #this is not efficient, might need improvement
    response = HttpResponse(content_type="image/png")
    new_image.save(response, "PNG")
    #patch_cache_control(response,{'no-transform':True,'public':True,'max-age':300,'s-maxage':900})
    return response

def route(request):
    color = request.GET.get('color', 'ffffff')
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)
    new_color = (red, green, blue)
    new_scale = float(request.GET.get('scale', '1.0'))

    #requires the images to be in MEDIA_ROOT
    base_img = Image.open('%s/%s' % (settings.MEDIA_ROOT,
                                    'base_route.png'))
    color_img = Image.open('%s/%s' % (settings.MEDIA_ROOT,
                                    'route_mask.png'))
    base_pixels = base_img.load()
    color_pixels = color_img.load()

    #change the color
    for y in xrange(color_img.size[1]):
        for x in xrange(color_img.size[0]):
            new_color = (new_color[0], new_color[1], new_color[2], 0)
            color_pixels[x,y] = new_color

    new_image = color_img.copy()
    new_img_data = new_image.load()
    for y in xrange(color_img.size[1]):
        for x in xrange(color_img.size[0]):
            new_red = color_pixels[x, y][0]
            new_green = color_pixels[x, y][1]
            new_blue = color_pixels[x, y][2]
            new_alpha = base_pixels[x, y][3]
            new_img_data[x, y] = (int(new_red), int(new_green), int(new_blue), int(new_alpha))

    new_image = new_image.resize((int(new_image.size[0] * new_scale), int(new_image.size[1] * new_scale)))

    new_image = new_image.resize((int(new_image.size[0] * new_scale), int(new_image.size[1] * new_scale)))

    #this is not efficient, might need improvement
    response = HttpResponse(content_type="image/png")
    new_image.save(response, "PNG")
    return response

def area(request):
    color = request.GET.get('color', 'ffffff')
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)
    new_color = (red, green, blue, 255)
    new_scale = float(request.GET.get('scale', '1.0'))

    #requires the images to be in MEDIA_ROOT
    base_img = Image.open('%s/%s' % (settings.MEDIA_ROOT,
                                    'base_area.png'))
        
    new_image = Image.new('RGBA',
                          (base_img.size[0],
                           base_img.size[1]),
                          new_color)
    base_pixels = base_img.load()
    new_img_data = new_image.load()
    a = 20
    for y in xrange(new_image.size[1]):
        for x in xrange(new_image.size[0]):
            new_red = new_img_data[x, y][0] - base_pixels[x, y][0] + a
            new_green = new_img_data[x, y][1] - base_pixels[x, y][0] + a
            new_blue = new_img_data[x, y][2] - base_pixels[x, y][0] + a
            new_alpha = base_pixels[x, y][1]
            new_img_data[x, y] = (int(new_red),
                                  int(new_green),
                                  int(new_blue),
                                  int(new_alpha))

    new_image = new_image.resize((int(new_image.size[0] * new_scale), int(new_image.size[1] * new_scale)))
    
    #this is not efficient, might need improvement
    response = HttpResponse(content_type="image/png")
    new_image.save(response, "PNG")
    return response

#views returning svg
def place_marker(request):
    color = request.GET.get('color', 'ffffff')
    scale = request.GET.get('scale', 1)
    
    return render_to_response('place_marker.svg',
                              {'color': '#%s' % color,
                               'scale': scale},
                              mimetype = 'image/svg+xml')

def route_marker(request):
    color = request.GET.get('color', 'ffffff')
    scale = request.GET.get('scale', 1)
    
    return render_to_response('route_marker.svg',
                              {'color': '#%s' % color,
                               'scale': scale},
                              mimetype = 'image/svg+xml')

def area_marker(request):
    color = request.GET.get('color', 'ffffff')
    scale = request.GET.get('scale', 1)
    
    return render_to_response('area_marker.svg',
                              {'color': '#%s' % color,
                               'scale': scale},
                              mimetype = 'image/svg+xml')
