from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home(request):
    data = {
        "slackUsername": "Curtizod",
        "backend": True,
        "age": 26,
        "bio": "I'm Chidozie Ogbuji, a backend intern of HNGi9",
    }

    return JsonResponse(data)
