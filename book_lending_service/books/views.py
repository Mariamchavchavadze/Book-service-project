from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Book, Author, Genre, BookStatus, Location, Interest
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, BookStatusSerializer, LocationSerializer, \
    InterestSerializer
from .filters import BookFilter  # We'll create this custom filter class
from rest_framework.response import Response



class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can manage books

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = (DjangoFilterBackend,)  # Enable filtering
    filterset_class = BookFilter  # Use the custom filter class

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]

class BookStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BookStatus.objects.all()
    serializer_class = BookStatusSerializer
    permission_classes = [permissions.AllowAny]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Prevent a user from expressing interest in a book they already own
        book = serializer.validated_data['book']
        if book.owner == self.request.user:
            raise serializers.ValidationError("You cannot express interest in your own book")
        serializer.save()

    def approve_interest(self, request, pk=None):
        # Approve a user's interest in a book
        interest = self.get_object()
        if interest.book.owner == request.user:
            interest.status = 'approved'
            interest.save()
            # Update book status
            interest.book.status = 'taken'
            interest.book.save()
            return Response({'status': 'Interest approved'})
        return Response({'error': 'You are not the owner of this book'}, status=status.HTTP_403_FORBIDDEN)

    def reject_interest(self, request, pk=None):
        # Reject a user's interest in a book
        interest = self.get_object()
        if interest.book.owner == request.user:
            interest.status = 'rejected'
            interest.save()
            return Response({'status': 'Interest rejected'})
        return Response({'error': 'You are not the owner of this book'}, status=status.HTTP_403_FORBIDDEN)
