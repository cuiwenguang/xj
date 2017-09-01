# encoding: utf-8
import os
import json
import numpy as np
import cv2
import face_recognition


def train_faces(file_path, json_file):
    '''初始化训练所有图片'''
    img_encoding = {}

    for i, img in enumerate(os.listdir(file_path)):

        if not img.endswith('.jpg'):
            continue

        face_image = face_recognition.load_image_file('%s/%s'% (file_path, img))
        faces = face_recognition.face_encodings(face_image)

        if not faces:
            print(" connot find face, please check img file" % img)
            continue

        face_encoding = faces[0]
        img_encoding[img] = face_encoding.tolist()

    if img_encoding:

        with open(json_file, 'w') as f:
            json.dump(img_encoding, f)

    else:
        print('not any photo encoding')


def new_face(img, dir_path):
    pass


def face_rec(image_file, json_file):
    '''头像识别'''
    img = np.fromstring(image_file.read(), np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    # img = cv2.imread(image_file)
    # small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)

    all_face_encodings = {}
    face_names ={}

    with open(json_file, 'r') as f :
        all_face_encodings = json.load(f)

    for face_encoding in face_encodings:
        for akey, avalue  in all_face_encodings.items():
            #match_dis = face_recognition.compare_faces([np.array(avalue)], face_encoding, tolerance=0.3)
            match_dis = face_recognition.face_distance([np.array(avalue)], face_encoding)
            if match_dis <= 0.4:
                face_names[akey] = match_dis

    if not face_names:
        print('Not match any face')
        return None

    min_dis = sorted(face_names.items(), key=lambda  d:d[1])

    if not min_dis :
        print('match value less than 0.3 ')
        return None

    return min_dis[0][0].replace('.jpg', '')


if __name__ == '__main__':
    path = '/Users/cui/Downloads/avatar/'
    json_file = '/Users/cui/projects/xj/app/faces.json'
    img_path = '/Users/cui/Downloads/avatar/65322219970301231X.jpg'
    train_faces(path, json_file)
    print face_rec(img_path, json_file)