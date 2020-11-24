from django.shortcuts import render
from .models import super
from django.db.models import Q
# Create your views here.
# To change handle the dstination from here
def index(request):
    if request.GET:
        print("Hello")
        query = request.GET["query"]
        dests = super.objects.filter(Q(city__icontains = query) | Q(hotel__contains=query) | Q(rating__icontains = query))
        return render(request, "search.html",{'dests':dests})   
    dests = super.objects.all()
    return render(request, "index.html", {'dests':dests})


def form(request):
    return render(request, "form.html")
def list(request):
    dests = super.objects.all()
    return render(request, "list.html", {'dests':dests})

    #return HttpResponse("Searching...")

def img(request):
    dests = super.objects.all()
    return render(request, "img.html", {"dests" : dests})