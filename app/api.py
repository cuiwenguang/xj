# -*- coding:utf-8 -*-
import json
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login,logout
from app.models import PersonnelProfile
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from xj.settings import FACE_CLASSIFIER
from .validate import face_rec

@csrf_exempt
def sign_in(request):
    '''用户登录接口'''

    json_data = json.loads(request.body.decode())
    username = json_data.get("username", "")
    password = json_data.get("password", "")
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return JsonResponse({
            "state": 200,
            "msg": "登录成功"
        })
    else:
        return JsonResponse({
            "state": 401,
            "msg": "未授权的用户",
            "data": None
        })
@csrf_exempt
def sign_out(request):
    '''用户注销'''
    logout(request)
    return JsonResponse({
        "state": 200,
        "msg": "注销完成",
    })

@csrf_exempt
def sign_up(request):
    json_data = json.loads(request.body.decode())
    username = json_data.get("username", "")
    password = json_data.get("password", "")
    email = "xj_" + username + "@admin.com"

    from django.contrib.auth.models import User, Group
    if User.objects.filter(Q(email=email) | Q(username=username)).exists():
        return JsonResponse({
            "state": 201,
            "msg": "用户已存在",
        })
    else:
        user = User.objects.create_user(username, email=email, password=password)
        return JsonResponse({
            "state": 200,
            "msg": "注册完成",
        })

@csrf_exempt
def face_recognition(request):
    '''头像识别接口'''

    if request.method == 'POST':
        img = request.FILES.get('imgFace')
        idcard = face_rec(img, '/' + FACE_CLASSIFIER)

        if idcard is None:
            return JsonResponse({
                "state": 200,
                "data": None,
                "msg": 'not match'
            })

        print(idcard)
        p = PersonnelProfile.objects.get(ID_number=idcard)

        return JsonResponse({
            "state": 200,
            "data": {
                "uuid": p.personnel_uuid,
                "name": p.name,
                "ID_number": p.ID_number,
                "ID_photo": p.ID_photo
            }
        })

    return HttpResponse({"state":401, "data": None}, status=401)