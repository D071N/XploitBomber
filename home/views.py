from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Attackinfo
from .models import Userinfo
from .models import Workerinfo
import multiprocessing
import time


def index(request):
    return  render(request,'index.html')

def doattack(request):
    import os

    mobile_no = request.POST.get("mn")
    frequency_no = request.POST.get("fq")

    try:
        if mobile_no == "" or int(frequency_no) < 0 or len(mobile_no) != 10 or frequency_no == "" or (frequency_no.isdigit() == False) or (mobile_no.isdigit() == False):
            messages.error(request, "Invalid Input ")
            return redirect("/")
    except:
        messages.error(request, "Error")
        return redirect("/")

    Producti = Attackinfo( mobile_n = mobile_no, frequency_n=frequency_no)
    Producti.save()

    if int(frequency_no) >= 5000 :
        frequency_no = "5000"

    #FOR WINDOWS
    # os.system(f"python bomber.py --num {frequency_no} {mobile_no}")

    #FOR LINUX SERVER(AWS)
    # os.system(f"nohup /home/ubuntu/env/bin/python3 bomber.py --num {frequency_no} {mobile_no}  &")

    #FOR HEROKU
    os.system(f"nohup /usr/bin/python3 bomber.py --num {int(frequency_no)*2} {mobile_no} &")
    messages.success(request, f"ATTACK STARTED AT {mobile_no}  WITH {frequency_no} SMS ")
    return redirect("/")