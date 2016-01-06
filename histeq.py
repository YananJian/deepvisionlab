import cvlib.cv2 as cv2
import os
import argparse

def histeq(img):
    rh, rw, rc = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = None
    img2 = cv2.equalizeHist(gray)
    cv2.imshow('img', gray)
    cv2.imshow('img2', img2)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Histogram equalizer')
    parser.add_argument('image_path', metavar='image_path', 
                                    help='path of the image that is to be calculated')
    args = parser.parse_args()
    img = cv2.imread(args.image_path)
    histeq(img)
