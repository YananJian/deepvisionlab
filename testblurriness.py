import cvlib.cv2 as cv2
import numpy as np
import argparse

face_cascade = cv2.CascadeClassifier('cvlib/haarcascade_frontalface_alt2.xml')

def get_blurriness(gray_img):
    blurriness = np.max(cv2.convertScaleAbs(cv2.Laplacian(gray_img,8)))
    print blurriness
    return blurriness

def get_face_region(gray_frame):
    results = []
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    for (x,y,w,h) in faces:
        results.append((x,y,w,h))
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test blurriness')
    parser.add_argument('image_path', metavar='image_path', 
                                    help='path of the image that is to be calculated')
    args = parser.parse_args()
    img = cv2.imread(args.image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = get_face_region(gray)
    for item in faces:
        x = item[0]
        y = item[1]
        w = item[2]
        h = item[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        blurriness = get_blurriness(gray[y:y+h, x:x+w])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Blurriness:' + str(blurriness),(x,y), font, 1,(255,255,255),2)
        cv2.imshow('img',img)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
