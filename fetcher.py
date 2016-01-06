import pafy
import hashlib
import argparse
import os

store_dir = './testvideos/'

def progress(total, recvd, ratio, rate, eta):
    print(recvd, ratio, eta)

def download(youtube_url):
    try:
        os.stat(store_dir)
    except:
        os.makedirs(store_dir)

    if youtube_url in [None, '']:
        print "Youtube URL is None, terminating..."
        return
    vobj = pafy.new(youtube_url)
    target_video = None
    for stream in vobj.streams:
        if stream.extension == 'mp4':
            target_video = stream
    if target_video is None:
        target_video = vobj.streams[0]
    print "Downloading %s.%s" % (target_video.title, target_video.extension)
    md5name = hashlib.md5(target_video.title.encode('utf-8')).hexdigest()
    store_name = store_dir + md5name+"." + target_video.extension
    target_video.download(filepath = store_name)
    print "Stored as : %s\n" % store_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Youtube Fetcher')
    parser.add_argument('URL', metavar='URL', 
                                    help='a Youtube URL to be downloaded')
    args = parser.parse_args()
    download(args.URL)

