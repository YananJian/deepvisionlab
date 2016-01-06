import cv2
import argparse
import os

def detect_human(img):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    found, w = hog.detectMultiScale(img)
    print found
    print w
    return found

def draw_detections(img, rects, thickness = 1): 
    for x, y, w, h in rects:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness)

    cv2.imshow('img', img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Human detector')
    parser.add_argument('image_path', metavar='image_path', 
                                    help='path of the image that is to be calculated')
    args = parser.parse_args()
    img = cv2.imread(args.image_path)
    rect = detect_human(img)
    if rect is not None:
        draw_detections(img, rect)
