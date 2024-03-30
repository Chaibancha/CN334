from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests


# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    
    return HttpResponse('Welcome to 6410742230 Chaibancha Raengklang views!')

def item_view(request, item_id):

    context_data = {
        "item_id": item_id   
        }
       
    return render(request, 'index.html',context= context_data)

@csrf_exempt
def basic_request(request):
    if request.method == "GET":
        return JsonResponse({"status":"GET Pass"}, safe=False)
    if request.method == "POST":
        return JsonResponse({"status":"POST Pass"}, safe=False)

@csrf_exempt
def tokenize(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"}, safe=False, status=500)
        url = "https://api.aiforthai.in.th/tlexplus"
        data = {'text':sentence}
        headers = {
        'Apikey': "RpbQ13NhJzyB8KuaH0S0lOYb96U6uDC0"
        }
        response = requests.post(url, data=data, headers=headers)
        reponse_json = response.json()
        return JsonResponse({"student":"student_id", "tokenize":reponse_json}, safe=False)
    return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)

@csrf_exempt
def sentiment(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"}, safe=False, status=500)
        url = "https://api.aiforthai.in.th/ssense"
        data = {'text':sentence}
        headers = {
        'Apikey': "RpbQ13NhJzyB8KuaH0S0lOYb96U6uDC0"
        }
        # try:
        #     response = requests.post(url, data=data, headers=headers)
        #     response_json = response.json()
        #     sentiment_data = response_json.get('sentiment', {})
        #     return JsonResponse({"sentiment": sentiment_data}, status=response.status_code)
        # except Exception as e:
        #     return JsonResponse({"error": str(e)}, status=500)
        try:
            response = requests.post(url, data=data, headers=headers)
            response_json = response.json()
            return JsonResponse({"student":"6410742230","sentiment": response_json}, status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)

import IPython
@csrf_exempt
def text2speech(request):
    if request.method == "POST":
        try:
            sentence = request.POST['text']
        except:
            return JsonResponse({"error":"Input not found"}, safe=False, status=500)
        url = "https://api.aiforthai.in.th/vaja9/synth_audiovisual"
        data = {'input_text':sentence,'speaker': 1, 'phrase_break':0, 'audiovisual':0}
        headers = {
        'Apikey': "RpbQ13NhJzyB8KuaH0S0lOYb96U6uDC0",
        'Content-Type' : 'application/json'
        }
        data = {'input_text':sentence,'speaker': -1, 'phrase_break':0, 'audiovisual':0}
        response = requests.post(url, json=data, headers=headers)
        print(response.json())
        
        # ดาวน์โหลดไฟล์เสียง
        resp = requests.get(response.json()['wav_url'],headers=headers)
        if resp.status_code == 200:
          with open('test.wav', 'wb') as a:
            a.write(resp.content)
            print('Downloaded: ')
            IPython.display.display(IPython.display.Audio('test.wav'))
        else:
          print(resp.reason)
        return JsonResponse({"student":"6410742230","Output": response.json()['wav_url']}, status=response.status_code)
        
    return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)