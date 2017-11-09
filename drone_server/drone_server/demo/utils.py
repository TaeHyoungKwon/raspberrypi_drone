import os
import time
import picamera


def make_foler_pictures():
    
    origin_pwd = os.getcwd()
    today = '171105'
    os.chdir("demo")
    os.chdir("pictures")
    os.chdir(today)
    
    cnt = len(os.listdir())
    file = open("{}.jpg".format(cnt+1), 'w')
    file.close()
    os.chdir(origin_pwd)

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('{}.jpg'.format(cnt+1), 'w')


def make_foler_record():
    
    origin_pwd = os.getcwd()
    today = '171106'
    os.chdir("demo")
    os.chdir("pictures")
    os.chdir(today)
    
    cnt = len(os.listdir())
    file = open("{}.mp4".format(cnt+1), 'w')
    file.close()
    os.chdir(origin_pwd)
    time.sleep(10)

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')


def make_foler_upload():
    print("\n")
    print("Upload...")

    for a in range(0,2):
        print(str(a) + " is uploading ...")
        time.sleep(1)

def go_streaming():
    os.system("stream.sh")