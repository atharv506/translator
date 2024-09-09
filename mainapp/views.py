from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from googletrans import Translator, constants
from pprint import pprint



def home(request):
    return render(request,'index.html')


def translate(request):
    if request.method == 'POST':
        text = request.POST['text']
        translator = Translator()

        translation = translator.translate(text)
        #print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

        org_text = translation.origin
        org_lg =  translation.src
        tr_text = translation.text
        tr_lg =  translation.dest


    return render(request,'translate.html',{'org_text':org_text,'org_lg':org_lg,'tr_text': tr_text,'tr_lg':tr_lg })