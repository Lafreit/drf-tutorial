# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()), # List and create view for snippets
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()), # Detail view for snippets
    path('users/', views.UserList.as_view()), # List and create view for users
    path('users/<int:pk>/', views.UserDetail.as_view()), # Detail view for users
]

urlpatterns = format_suffix_patterns(urlpatterns)