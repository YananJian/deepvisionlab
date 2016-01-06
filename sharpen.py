import cvlib.cv2 as cv2
import numpy as np
import argparse

def sharpen(img):
    rh, rw, rc = img.shape
    img2 = np.zeros((rh, rw, 3), dtype=np.uint8);
    kernel_size = 3
    scale = 1
    delta = 0
    ddepth = cv2.CV_64F
    img2 = cv2.convertScaleAbs(cv2.Laplacian(img,ddepth,ksize = kernel_size,scale = scale,delta = delta))
    
    sharpened = cv2.addWeighted(img, 1, img2, -0.5, 0)
    cv2.imshow('original img', img)
    cv2.imshow('sharpened img', sharpened)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test blurriness')
    parser.add_argument('image_path', metavar='image_path', 
                                    help='path of the image that is to be calculated')
    args = parser.parse_args()
    img = cv2.imread(args.image_path)
    sharpen(img)
