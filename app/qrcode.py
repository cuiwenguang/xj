# -*- coding:utf-8 -*-
import json
import qrcode
import os

def generate(data):
    '''生成二维码的方法'''
    images_path = os.getcwd() + '/static/qrimage/'
    file_name = '_'.join([data["name"], data["uuid"]]) + '.jpg'
    try:
        if not os.path.exists(images_path):
            os.makedirs(images_path)
        # destination = open(images_path + file_name, 'wb+')
        # img = qrcode.make("some date here")
        # img.save(destination, 'JPEG')
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        content = json.dumps(data).encode("utf-8")
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(images_path + file_name)
        return file_name
    except Exception as e:
        print(e)

    # 二维码路径保存回数据库

