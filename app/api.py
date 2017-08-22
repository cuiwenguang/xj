import json
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login,logout

from .qrcode import generate

def sign_in(request):
    '''用户登录接口'''
    json_data = json.loads(request.body)
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

def sign_out(request):
    '''用户注销'''
    logout()
    return JsonResponse({
        "state": 200,
        "msg": "注销完成",
    })

def qrcode_generate(request):
    '''测试生成二维码'''
    try:
        data = "sdfasasdsdds" # 用户uuid
        generate(data)
        return JsonResponse({"state": 200, "msg": "完成", "data": "/static/qrimage/"+data +".jpg"})
    except:
        return JsonResponse({"state":500, "msg": "发生错误", "data": None})

