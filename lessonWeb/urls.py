
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include("servis.urls")),
    path('webLib/', include('webLib.urls')),
    path('admin/', admin.site.urls),
]
