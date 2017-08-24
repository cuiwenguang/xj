# -*- coding:utf-8 -*-
import json
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login,logout
from .qrcode import generate,analysis
from app.models import PersonnelProfile
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

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

def qrcode_generate(request):
    '''测试生成二维码'''
    try:
        pers = PersonnelProfile.objects.exclude(ID_number='').exclude(name='')[0:3]
        for per in pers:
            data = {
                "uuid": per.personnel_uuid,
                "name": per.name,
                "ID_number": per.ID_number,
                "ID_photo": per.ID_photo
            }
            path_file = generate(data)
        return JsonResponse({"state": 200, "msg": "完成", "data": path_file})
    except Exception as e:
        return HttpResponse(e)

def qrcode_analysis(request):
    '''测试解析二维码'''
    try:
        data = analysis()
        return JsonResponse({"state": 200, "msg": "完成", "data": data})
    except Exception as e:
        return HttpResponse(e)