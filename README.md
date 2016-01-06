# deepvisionlab
============
This is the collection of experiments I'm running now.
-----------
fetcher.py downloads youtube video to ./testvideos.
```
python fetcher.py https://www.youtube.com/watch?v=nfWlot6h_JM
```

-----------
sampler.py samples the downloaded video.
```
python sampler.py [video path] [store path]
python sampler.py -h
```

-----------
sharpen.py sharpens the given img.
```
python sharpen.py [image path]
python sharpen.py -h
```

-----------
testblurriness.py calculates blurriness of a given img.
```
python testblurriness.py [image path]
```

-----------
humandetector_haar.py detects people using haarcascade, it works better than hog
```
python humandetector_haar.py [image path]
```

-----------
humandetector_hog.py detects people using HOG, I don't know why it performs bad on my images
```
python humandetector_hog.py [image path]
```

------------
histeq.py performs histogram equalization on the given image.
```
python histeq.py [image path]
```

------------
cvlib contains opencv libraries
