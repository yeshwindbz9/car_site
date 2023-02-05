from django.urls import path
from .views import *

app_name = "cars"
urlpatterns = [
    path("", list_view, name="list"),
    path("add/", add_view, name="add"),
    path("delete/", delete_view, name="delete"),
]
