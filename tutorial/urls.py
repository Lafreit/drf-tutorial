# tutorial/urls.py
from django.contrib import admin # Import admin module
from django.urls import include, path # Import include function

urlpatterns = [
    path('admin/', admin.site.urls), # Admin site URL
    path('api-auth/', include('rest_framework.urls')), # Include DRF auth URLs
    path('', include('snippets.urls')), # Include snippets app URLs
]
