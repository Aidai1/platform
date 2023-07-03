# Generated by Django 4.2.3 on 2023-07-03 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('category_description', models.TextField()),
                ('category_slug', models.SlugField(max_length=100, unique=True)),
                ('timcde', models.DateTimeField(auto_now_add=True, max_length=120)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100, verbose_name='Название цвета')),
                ('color_slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Цвет товара ',
                'verbose_name_plural': 'Цвета товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ширина')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Длина')),
                ('thickness', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Толшина')),
            ],
            options={
                'verbose_name': 'Размер товара',
                'verbose_name_plural': 'Размеры товаров',
            },
        ),
        migrations.CreateModel(
            name='RSSSubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telegram_id', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Подписка на RSS',
                'verbose_name_plural': 'Подписки на RSS',
            },
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacanc', models.CharField(max_length=120, verbose_name='Должность')),
                ('salary', models.CharField(max_length=120, verbose_name='Зарплата')),
                ('vac_description', models.CharField(max_length=120, verbose_name='Описание')),
                ('vac_slug', models.SlugField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название товара')),
                ('product_description', models.TextField()),
                ('prod_slug', models.SlugField(max_length=120, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/')),
                ('prod_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcolor')),
                ('prod_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productsize')),
            ],
        ),
    ]