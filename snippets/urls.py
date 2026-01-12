# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'), # List and create view for snippets
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'), # Detail view for snippets
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'), # Highlight view for snippets
    path('users/', views.UserList.as_view(), name='user-list'), # List and create view for users
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'), # Detail view for users
    path('', views.api_root, name='api-root'), # Root API endpoint
]

urlpatterns = format_suffix_patterns(urlpatterns)