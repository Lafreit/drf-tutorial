# snippets/views.py
from django.contrib.auth.models import User # For user model
from rest_framework import generics, permissions # For generic views and permissions

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer # Import UserSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView): # View for listing and creating snippets
    queryset = Snippet.objects.all() # Queryset for all snippets
    serializer_class = SnippetSerializer # Serializer for Snippet model
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # Set permissions

    def perform_create(self, serializer): # Assign owner on creation
        serializer.save(owner=self.request.user) # Set the owner to the logged-in user

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView): # View for snippet detail
    queryset = Snippet.objects.all() # Queryset for all snippets
    serializer_class = SnippetSerializer # Serializer for Snippet model
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # Set permissions

class UserList(generics.ListAPIView): # View for listing users
    queryset = User.objects.all() # Queryset for all users
    serializer_class = UserSerializer # Serializer for User model

class UserDetail(generics.RetrieveAPIView): # View for user detail
    queryset = User.objects.all() # Queryset for all users
    serializer_class = UserSerializer # Serializer for User model