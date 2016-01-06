import numpy as np
import cvlib.cv2 as cv2
import os
import time
import argparse

face_cascade = cv2.CascadeClassifier('cvlib/haarcascade_frontalface_alt2.xml')

def show_face_body(img):
    xcrop_bias = 50
    body_head_portion = 5

    start = time.time()
    rh, rw, rc = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if y+h*2 > rh:
            continue
        crop_img = img[y+h:y+h*body_head_portion, x-xcrop_bias:x+w+xcrop_bias]
        cv2.rectangle(img, (x-xcrop_bias,y+h), (x+w+xcrop_bias, y+h*body_head_portion), (0, 255, 0), 2)
        #cv2.imwrite(img_path+'/'+f+'_'+str(ct)+'.jpg', crop_img)
    cv2.imshow('img',img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    end = time.time()
    print 'total time consumed: %d'%int(end - start)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Face detector')
    parser.add_argument('image_path', metavar='image_path', 
                                    help='path of the image that is to be calculated')
    args = parser.parse_args()
    img = cv2.imread(args.image_path)
    show_face_body(img)

