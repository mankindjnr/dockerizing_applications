from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    resp = requests.get("http://fastapi:9400")
    print(resp.json())
    return render(request, "start/index.html")


def about(request):
    return render(request, "start/index.html")
