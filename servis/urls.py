from django.urls import path, re_path
from servis.views import index, page, about, jsonShow


urlpatterns = [
    path('', index, name="service"),
    re_path(r'^service/(?P<pageNum>[0-9]{3})/$', page),
    path("about/<int:id>", about, name="about"),
    path("json", jsonShow, name="jsonShow"),
]


