from django.shortcuts import render

# Create your views here
def hello(request):
    return HttpResponse("Hello world ! ")