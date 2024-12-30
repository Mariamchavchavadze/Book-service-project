from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import BookViewSet, AuthorViewSet, GenreViewSet, BookStatusViewSet, CustomTokenObtainPairView, \
    LocationViewSet, InterestViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'book-status', BookStatusViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'interests', InterestViewSet)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('interests/<int:pk>/approve/', InterestViewSet.as_view({'patch': 'approve_interest'}), name='approve_interest'),
    path('interests/<int:pk>/reject/', InterestViewSet.as_view({'patch': 'reject_interest'}), name='reject_interest'),

]
