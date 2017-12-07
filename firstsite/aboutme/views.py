from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'aboutme/home.html')

def contact(request):
    return render(request, 'aboutme/basic.html' , {'content': ['If you would like to contact me, please email me', 'blah@vlah.com']})
