from django.urls import path
from django.http import HttpResponse

def ping(request):
    return HttpResponse('pong')

urlpatterns = [
    path('ping/', ping),
]
