from django.http import HttpResponse
from django.shortcuts import render
import os


file_path=os.path.abspath(__file__)
dir_path=os.path.dirname(os.path.dirname(file_path))

def index(request):
    return HttpResponse("<marquee direction=\"right\"><h1>welcome to my world</h1></marquee>")

def htmlrespo(request):
    file_dir=os.path.join(dir_path,"sample.html")
    fp=open(file_dir, "r")
    data=fp.read()
    return HttpResponse(data)

def rend1(request):
    return render(request, "sample.html")
