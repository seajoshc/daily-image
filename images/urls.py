from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = "images"

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^image/(?P<image_id>\d+)/?$", views.detail, name="detail"),
    path("search/", views.search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
