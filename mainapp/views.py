import datetime

from django.shortcuts import render


def main(request):
    title = "home"
    return render(request, "mainapp/index.html")


def shop(request):
    return render(request, "mainapp/shop.html")


def contact(request):
    return render(request, "mainapp/contact.html")
