from django.shortcuts import render

# Create your views here.

def  forloop(request):
    d={ 'name':'samanuyam'}
    return render(request,'forloop.html',d)