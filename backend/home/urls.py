from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("Api.urls")),
    path("api/products/", include("products.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v2/", include("home.routers"))
]
