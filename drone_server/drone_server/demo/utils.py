import os
import time
import picamera

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def make_foler_pictures():
    
    origin_pwd = os.getcwd()
    today = datetime.date.today()
    os.chdir("demo")
    os.chdir("pictures")
    os.chdir(today)
    
    cnt = len(os.listdir())
    os.chdir(origin_pwd)

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture("{}.jpg".format(cnt+1), 'w')


def make_foler_record():
    
    origin_pwd = os.getcwd()
    today = datetime.date.today()
    os.chdir("demo")
    os.chdir("pictures")
    os.chdir(today)
    
    cnt = len(os.listdir())
    os.chdir(origin_pwd)
    time.sleep(10)

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.recording("{}.mp4".format(cnt+1), 'w')


def make_foler_upload():
    try :
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()

    if not creds or creds.invalid:
        print("make new storage data file ")
        flow = client.flow_from_clientsecrets('client_secret_drive.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)

    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    FILES = (
       
    )

    for file_title in FILES :
        file_name = file_title
        metadata = {'name': file_name,
                    'mimeType': None
                    }

        res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
        if res:
            print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))

def go_streaming():
    os.system("stream.sh")