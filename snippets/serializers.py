# snippets/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html'
    )

    class Meta:
        model = Snippet
        fields = (
            "url", # URL of the snippet
            "id", # ID of the snippet
            "highlight", # Highlight URL
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner", # Owner of the snippet
        )

class UserSerializer(serializers.HyperlinkedModelSerializer): # Serializer for User model
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True # Read-only field for user's snippets
    )

    class Meta:
        model = User
        fields = ("url", "id", "username", "snippets") # Fields for User model