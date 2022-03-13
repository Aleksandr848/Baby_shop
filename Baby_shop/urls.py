from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main),
    path("shop/", mainapp.shop),
    path("contact/", mainapp.contact),

    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("shop/", mainapp.shop, name="shop"),
    path("contact/", mainapp.contact, name="contact"),
]
