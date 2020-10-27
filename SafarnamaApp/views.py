from django.shortcuts import render
# Create your views here.
# To change handle the dstination from here
def index(request):
    return render(request, "index.html")
