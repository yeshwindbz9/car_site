from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *


# Create your views here.
def list_view(request):
    all_cars = Car.objects.all()
    context = {"all_cars": all_cars}
    return render(request, "cars/list.html", context=context)


def add_view(request):
    if request.POST:
        brand = request.POST["brand"]
        model = request.POST["model"]
        year = int(request.POST["year"])
        Car.objects.create(
            brand=brand,
            model=model,
            year=year,
        )
        return redirect(reverse("cars:list"))
    else:
        return render(request, "cars/add.html")


def delete_view(request):
    if request.POST:
        id = request.POST["id"]
        try:
            Car.objects.get(pk=id).delete()
            return redirect(reverse("cars:list"))
        except:
            print("no id found")
            return redirect(reverse("cars:list"))
    else:
        return render(request, "cars/delete.html")
