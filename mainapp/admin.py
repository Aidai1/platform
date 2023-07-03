from django.contrib import admin


from .models import Product, Category, ProductColor, ProductSize, Vacancies, RSSSubs

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_description', 'prod_color', 'prod_size', 'image', 'prod_slug' )
    list_display_links = ('id', 'name')
    prepopulated_fields = {'prod_slug': ('name')}
    ordering = ('name', 'prod_color', 'prod_size', )
    list_filter  = ('id', 'product_description', 'prod_color', 'prod_size')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description', 'category_slug', 'time')
    list_display_links = ('id', 'category_name') 
    prepopulated_fields = {'category_slug': ('category_name')} 
    ordering = ['category_name', 'create_ad', ]
    list_filter = ('id','category_name', 'time')

class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug' )   
    list_display_links =  ('id', 'name')
    prepopulated_fields = {'name': ('slug')} 
    list_filter = ('id','name')

      
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'width', 'length', 'thickness', )
    list_display_links = ('id', 'width', 'length', 'thickness')

class VacanciesAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name_vacanc', 'salary', 'vac_description', 'vac_slug')  
    list_display_links = ('id','name_vacanc', 'salary')
    list_filter = ('name_vacanc', 'salary')
    list_filter = ('name_vacanc', 'salary')


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(Vacancies)
admin.site.register(RSSSubs)
