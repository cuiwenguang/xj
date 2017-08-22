import json
import uuid
import  qrcode

from xj.settings import QRCODE_PATH

def generate(content):
    '''生成二维码的方法'''
    path = ''.join([QRCODE_PATH, content, '.jpg'])
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    img = qr.make(json.dumps(content))
    img.save(path)
    # 二维码路径保存回数据库


