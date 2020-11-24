from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("form", views.form, name="form.html"),
    path("list", views.list, name="list.html"),
    path("img", views.img, name="img")
]
