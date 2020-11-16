from django.urls import path
from . import views
urlpatterns=[
    path("form/", views.form, name="form.html"),
    path("list", views.list, name="list.html")
]
