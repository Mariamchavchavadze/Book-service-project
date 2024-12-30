from rest_framework import serializers
from .models import UserProfile, Author, Genre, BookStatus, Book, Location, Interest



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'bio']  # Customize based on fields you want to expose


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStatus
        fields = ['id', 'status']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'description']

class InterestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Interest
        fields = ['user', 'status']
# Serializer for Book
class BookSerializer(serializers.ModelSerializer):
    # Use primary key fields to avoid nested serialization and conflicts
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=BookStatus.objects.all())
    owner = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'status', 'description', 'owner','location','owner', 'status', 'interests']
