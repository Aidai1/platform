from django.db import models

class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категории', max_length=100)
    category_description = models.TextField()
    category_slug = models.SlugField(max_length=100, unique=True)
    # create_ad = models.DateTimeField(auto_now_add=True)
    timcde = models.DateTimeField(max_length=120,auto_now_add=True)
    
    def __str__(self):
        return f'{self.category_name}, {self.category_description}, {self.create_ad}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductSize(models.Model):
    width = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Ширина')
    length = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Длина')
    thickness = models.DecimalField(max_digits=10,decimal_places=2, verbose_name='Толшина')

     
    class Meta:
        verbose_name = 'Размер товара'
        verbose_name_plural = 'Размеры товаров'



class ProductColor(models.Model):
    color_name = models.CharField(max_length=100, verbose_name='Название цвета')
    color_slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.color_name
    
    class Meta:
        verbose_name = 'Цвет товара '
        verbose_name_plural = 'Цвета товаров'    

class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название товара')
    product_description = models.TextField() 
    prod_slug = models.SlugField(max_length=120, unique=True)       
    prod_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    prod_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

class Vacancies(models.Model):
    name_vacanc = models.CharField(max_length=120, verbose_name='Должность')
    salary =  models.CharField(max_length=120, verbose_name='Зарплата')
    vac_description = models.CharField(max_length=120, verbose_name='Описание')
    vac_slug = models.SlugField(max_length=120, unique=True)

    def __str__(self) -> str:
        return f'{self.name_vacanc} , {self.salary}'

class RSSSubs(models.Model):
    email = models.EmailField(null=True, blank=True)
    telegram_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.telegram_id}'

    class Meta:
        verbose_name = 'Подписка на RSS'
        verbose_name_plural = 'Подписки на RSS'  


