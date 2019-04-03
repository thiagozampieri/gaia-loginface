from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import gaia.config as cfg
import json

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('index.html')
    context = { 
        'title'     : 'Gaia Thanos - LoginFace',
        'STATIC_URL': settings.STATIC_URL,
        'cfg'       : json.dumps(cfg.options())
    }
    return HttpResponse(template.render(context, request))