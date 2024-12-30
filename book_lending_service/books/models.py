from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User


# Custom user model for extended user info
class UserProfile(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    # Fix for conflicting fields
    groups = models.ManyToManyField(Group, related_name='userprofile_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='userprofile_set', blank=True)

    def __str__(self):
        return self.username

# Author model
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Genre model
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Status model (available, reserved, etc.)
class BookStatus(models.Model):
    status = models.CharField(max_length=50, choices=[
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('reserved', 'Reserved')
    ])

    def __str__(self):
        return self.status
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    status = models.ForeignKey(BookStatus, related_name='books', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(UserProfile, related_name='owned_books', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, related_name="owned_books", on_delete=models.CASCADE)
    status = models.CharField(max_length=50,
                              choices=[('available', 'Available'), ('taken', 'Taken'), ('pending', 'Pending')],
                              default='available')

    def __str__(self):
        return self.title

class Interest(models.Model):
    book = models.ForeignKey(Book, related_name='interests', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='interested_books', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    def __str__(self):
        return f"{self.user.username} is interested in {self.book.title}"
