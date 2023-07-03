from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Category, Product, ProductSize, ProductColor, Vacancies

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_description')


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ('id', 'width', 'length', 'thickness', )     


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ('id','color_name', 'color_slug', ) 



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_description', 'prod_size', 'prod_color', )


class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ('id', 'name_vacanc', 'salary', 'vac_description', 'vac_slug', )