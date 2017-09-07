# -*- coding:utf-8 -*-
import json
import qrcode
import os
import base64
import StringIO
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
            box_size=2,
            border=1
        )
        #content = json.dumps(data)
        content = data['uuid']
        #content64 = base64.b64encode(content)
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image()
        # 改变颜色
        #img = img.convert("RGBA")
        img.save(images_path + file_name)
        return file_name
    except Exception as e:
        print(e)

    # 二维码路径保存回数据库


def analysis():
    '''解析二维码'''
    from PIL import Image
    import zbarlight

    file_path = os.getcwd() + '/static/qrimage/' + '吐尔逊喀热·木萨_60f3d152-865c-11e7-9df3-acbc3278f361.jpg'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    codes = zbarlight.scan_codes('qrcode', image)
    content = base64.b64decode(codes[0])
    print('QR codes: %s' % content)
    return content
