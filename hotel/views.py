from django.shortcuts import render
# Create your views here.
# To change handle the dstination from here
def form(request):
    return render(request, "form.html")
def list(request):
    return render(request, "list.html")

