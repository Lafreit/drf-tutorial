# snippets/views.py
from django.contrib.auth.models import User # For user model
from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer # Import UserSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView): # View for listing and creating snippets
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView): # View for snippet detail
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView): # View for listing users
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): # View for user detail
    queryset = User.objects.all()
    serializer_class = UserSerializer