from django.shortcuts import render
from .models import super, Profile
from django.db.models import Q
from .filters import SuperFilter
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
    if request.GET:
        query = request.GET["query"]
        dests = super.objects.filter(Q(city__icontains = query) | Q(hotel__contains=query) | Q(rating__icontains = query))
        return render(request, "list.html",{'dests':dests})   
    dests = super.objects.all()
    return render(request, "list.html", {'dests':dests})
    #return HttpResponse("Searching...")

def img(request):
    dests = super.objects.all()
    return render(request, "img.html", {"dests" : dests})

def profile(request):
    profs = Profile.objects.all()
    return render(request, "profile.html", {'profs': profs})

def delete(request, id ):
    profs = Profile.objects.get(id=id)
    profs.delete()
    auth.logout(request)
    return redirect("/")