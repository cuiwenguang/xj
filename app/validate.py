import numpy as np
import cv2

from xj.settings import FACE_CLASSIFIER

def detect_face(image_file):
    '''人脸检查，返回人脸坐标'''

    img = np.fromstring(image_file.read(), np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    face_cascade = cv2.CascadeClassifier(FACE_CLASSIFIER)
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    result = []
    for(x, y, width, height) in faces:
        result.append((x, y, x+width, y+height))
    
    return result


def draw_face(image_file):
    faces = detect_face(image_file)

    
