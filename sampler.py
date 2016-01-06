import cvlib.cv2 as cv2
import numpy as np
import argparse
import os

'''
Histogram equalization

'''
face_cascade = cv2.CascadeClassifier('cvlib/haarcascade_frontalface_alt2.xml')

def normalize_frame(frame):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #normalized_frame = cv2.equalizeHist(gray)
    pass

def get_gray_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

def is_blurred(gray_frame, threshold):
    blurness = np.max(cv2.convertScaleAbs(cv2.Laplacian(gray_frame,cv2.CV_64F)))
    if(blurness > threshold):
        return False
    else:
        return True

def get_face_region(gray_frame):
    results = []
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    for (x,y,w,h) in faces:
        results.append((x,y,w,h))
    return results

def start_sampling(vpath, ipath):
    try:
        os.stat(ipath)
    except:
        os.makedirs(ipath)  

    cap = cv2.VideoCapture(vpath)

    rval = True
    last_mean = 0
    threshold = 4
    while rval:
        rval, frame = cap.read()
        if frame is None:
            break
        width = frame.shape[0]
        height = frame.shape[1]
    
        frame_mean = np.sum(frame) / float(width * height * 3)
        if abs(frame_mean - last_mean) < threshold:
            print "frame_mean : %d - last_mean: %d < threshold: %d, ignoring..." % (frame_mean, last_mean, threshold)
            last_mean = frame_mean
            continue
       
        gray_frame = get_gray_frame(frame)
        if is_blurred(gray_frame, 200):
            continue
        faces = get_face_region(gray_frame)
        blurry = True
        if len(faces) == 0:
            continue
        else:
            for item in faces:
                x = item[0]
                y = item[1]
                w = item[2]
                h = item[3]
                if not is_blurred(gray_frame[y:y+h, x:x+w], 100):
                    blurry = False
                    break
        if not blurry: 
            print "frame_mean: %s, above threshold, saved." % str(frame_mean)
            cv2.imwrite(ipath + '/' + str(int(cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES))) + '.jpg',frame)

        last_mean = frame_mean
    frame_count = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    print "Read %d frames from video." % frame_count
    cap.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Video sampler')
    parser.add_argument('video_path', metavar='video_path', 
                                    help='path of the video that is to be sampled')
    parser.add_argument('store_path', metavar='store_path', 
                                    help='path that is going to store the sampled results')
    args = parser.parse_args()
    start_sampling(args.video_path, args.store_path)
