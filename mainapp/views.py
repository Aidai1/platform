

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins, generics, permissions
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import Category, Product, ProductSize, ProductColor, Vacancies
from .serializers import CategorySerializer, ProductSerializer, ProductSizeSerializer, ProductColorSerializer, UserSerializer, VacanciesSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly)


class ProductSizeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset= ProductSize.objects.all()
    serializer_class = ProductSizeSerializer
    permission_classes = (IsAdminOrReadOnly,)      


class ProductColorViewSet(viewsets.ModelViewSet):
    queryset =ProductColor.objects.all()
    serializer_class = ProductColorSerializer
    permission_classes = (IsAdminOrReadOnly)      


class VacanciesViewSet(viewsets.ModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = (IsAdminOrReadOnly)

