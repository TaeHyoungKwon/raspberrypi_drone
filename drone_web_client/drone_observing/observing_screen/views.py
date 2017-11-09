from django.shortcuts import render,HttpResponse
import requests
import os



'''
카메라 버튼을 누르면, 사진촬영이되고,
동영상 버튼을 누르면, 동영상 촬영이 되도록 한다.

카메라 버튼을 누르면 1번을 리턴, 동영상 버튼을 누르면 2번을 리턴하는데, form을 통해서 몇분 동안
촬영할 것인지도 같이 보내준다.
'''


def screen(request):
    if request.method =='POST':
        
        val = request.POST.dict()
        print(val)
        data = val['camera']

        if data == 'Capture':
            data = {"val" : data}
            response = requests.post('http://192.168.43.129:8000', data = data)

        else:
            if val.get('minute','None') != 'None':
                data = {"val" : data, "arg" : val['minute']}
                print("record")
                response = requests.post('http://192.168.43.129:8000', data = data)
            elif val.get('f_name','None') != 'None':
                data = {"val": data, "arg" : val['f_name']}
                print("upload")
                response = requests.post('http://192.168.43.129:8000', data = data)
            else:
                data = {"val" : data, "arg" : 'streaming'}

                print("stream")
                
                response = requests.post('http://192.168.43.129:8001', data = data)
                os.system('stream_client')

            

    else:
        print("GET")
    return render(request,"observing_screen/index.html",{})


