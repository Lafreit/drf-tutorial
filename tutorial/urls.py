# tutorial/urls.py
from django.contrib import admin
from django.urls import include, path # Import include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')), # Include snippets app URLs
]
