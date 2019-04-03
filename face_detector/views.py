from django.shortcuts import render

# Create your views here.
import numpy as np
import urllib
import json
import cv2
import os
from django.conf import settings
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import gaia.image as image
import gaia.filter as filter
import gaia.recognition as recognition
import gaia.people as model
import gaia.resize as resize
import gaia.utils as utils

from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

recognizer = recognition.face_recognizer()
recognizer.read('data/trainer.yml')
people = model.all()



@csrf_exempt
def requested_url(request):
    default = {"safely_executed": False}
    if request.method == "POST":
        if request.FILES.get("image", None) is not None:
            frame = image.read(stream = request.FILES["image"])
        else:
            url_provided = request.POST.get("url", None)
            
            if url_provided is None:
                default["error_value"] = "There is no URL Provided"

                return JsonResponse(default)

            frame = image.read(url = url_provided)

        (frame, all_faces) = recognition.recognition(frame)
        
        users = []
        faces = []
        for rect in all_faces:
            image_temp = resize.compare(frame, rect)
            (id, confidence) = recognizer.predict(image_temp)  
            
            if len(people) >= id:
                faces.append(rect)
                data_person = utils.MyEncoder().encode(people[id])
                users.append(data_person)

        faces=[(int(a), int(b), int(c), int(d)) for (a,b,c,d) in faces]

        default.update({"#of_faces": len(faces),
                        "faces": faces,
                        "users": users,
                        "safely_executed": True })

    return JsonResponse(default)

def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        user = User.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            request.session['member_id'] = user.id
            if user is not None and user.is_active:
                request.user = user
                auth_login(request, user)
            return HttpResponseRedirect('/admin/')
    except User.DoesNotExist:
        return HttpResponseRedirect('/')