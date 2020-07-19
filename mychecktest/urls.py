from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('check/', include('check.urls')),
    path('admin/', admin.site.urls),
]
