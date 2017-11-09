from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
import picamera

@csrf_exempt
def index(request):
    if request.method == "POST":
        url_dict = request.POST.dict()
        
        if url_dict['val'] == 'Capture':
            make_foler_pictures() 
            print("사진찍기 완료!")
            
        elif url_dict['val'] == 'Record':
            make_foler_record()
            print("영상찍기 완료!")

        elif url_dict['val'] == 'Upload':
            d_date = url_dict['date']
            make_foler_upload(d_date)
            time.sleep(3)
            print("업로드 완료!")

            

    return HttpResponse("<h1>Hello World!</h1>")
