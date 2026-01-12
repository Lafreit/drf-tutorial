# snippets/views.py
from django.contrib.auth.models import User # For user model
from rest_framework import generics, permissions, renderers # Import generics, permissions, and renderers from DRF
from rest_framework.decorators import api_view # For API view decorator
from rest_framework.response import Response # For API responses
from rest_framework.reverse import reverse # For reversing URLs

from .models import Snippet # Import Snippet model
from .permissions import IsOwnerOrReadOnly # Import custom permission
from .serializers import SnippetSerializer, UserSerializer # Import UserSerializer

# Create your views here.
class SnippetHighlight(generics.GenericAPIView): # View for highlighting snippets
    queryset = Snippet.objects.all() # Queryset for all snippets
    renderer_classes = (renderers.StaticHTMLRenderer,) # Use static HTML renderer

    def get(self, request, *args, **kwargs): # GET method
        snippet = self.get_object() # Get the snippet object
        return Response(snippet.highlighted) # Return the highlighted snippet

@api_view(['GET']) # API view for root endpoint
def api_root(request, format=None): # Function for API root
    return Response({ # Return a response with links to users and snippets
        'users': reverse('user-list', request=request, format=format), # Link to user list
        'snippets': reverse('snippet-list', request=request, format=format) # Link to snippet list
    })
class SnippetList(generics.ListCreateAPIView): # View for listing and creating snippets
    queryset = Snippet.objects.all() # Queryset for all snippets
    serializer_class = SnippetSerializer # Serializer for Snippet model
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # Set permissions

    def perform_create(self, serializer): # Assign owner on creation
        serializer.save(owner=self.request.user) # Set the owner to the logged-in user

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView): # View for snippet detail
    queryset = Snippet.objects.all() # Queryset for all snippets
    serializer_class = SnippetSerializer # Serializer for Snippet model
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, # Set permissions
        IsOwnerOrReadOnly, # Custom permission
                          ) # End of permission_classes

class UserList(generics.ListAPIView): # View for listing users
    queryset = User.objects.all() # Queryset for all users
    serializer_class = UserSerializer # Serializer for User model

class UserDetail(generics.RetrieveAPIView): # View for user detail
    queryset = User.objects.all() # Queryset for all users
    serializer_class = UserSerializer # Serializer for User model