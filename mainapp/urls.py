from rest_framework import routers
from django.urls import path, include

from .serializers import CategorySerializer, ProductColorSerializer, ProductSerializer, ProductSizeSerializer, VacanciesSerializer
from .views import CategoryViewSet, ProductViewSet, ProductSizeViewSet, ProductColorViewSet, VacanciesViewSet

app_name = 'ainek'

router = routers.DefaultRouter()

router.register(r'category-list', CategoryViewSet, basename='category-list')
router.register(r'product-list', ProductViewSet, basename='product-list')
router.register(r'productsize-list', ProductSizeViewSet, basename='productsize-list')
router.register(r'rss-subs', ProductColorViewSet, basename='rss-subs')
router.register(r'vacancies-list', VacanciesViewSet, basename='vacancies-list')



urlpatterns = [
    path('', include(router.urls)),
    # path('users/', UserListView.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    # path('redirect-to-telegram-bot/', RedirectToTelegramBoView.as_view(), name='redirect-to-telegram-bot'),
]