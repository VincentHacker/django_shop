# записать в requirements.txt
'''
Django
djangorestframework
psycopg2-binary # чтобы 
Pillow #чтобы проект мог с картинками работать
'''
# устанавливаем вирт.окружение и активируем
'''
atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ python3 -m venv env
atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ source env/bin/activate
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ 
'''

# Если не появилось окно, то Ctrl+Shift+P и набрать >python select и выбрать окружение

# Для развертки проекта
'''django-admin startproject shop .'''

# Появится manage.py, самый главный документ, с помощью которой ведется работа в django

# создаем составные части - приложения (создаются папки)
'''
\(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ python manage.y startapp accounts
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ python manage.py startapp product
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ python manage.py startapp orders
'''
# создаем БД в postgres
'''
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ psql -U test_user
Password for user test_user: 
psql (14.4 (Ubuntu 14.4-1.pgdg20.04+1))
Type "help" for help.

test_user=# create database shop;
CREATE DATABASE
'''
# добавить в settings.py в папке shop в раздел INSTALLED APP добавленные accounts, product, orders
'''
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework', 

    'accounts',
    'product',
    'orders'
]
'''
# настроим databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #django.db.backends.sqlite3
        'NAME': 'shop', #BASE_DIR / 'db.sqlite3',
        'HOST': 'localhost',
        'PORT': 5432,
        'USER': 'test_user',
        'PASSWORD': '1'
    }
'''
# настроим язык и timezone
'''
LANGUAGE_CODE = 'en-us' # можно поменять на ru

TIME_ZONE = 'Asia/Bishkek' #'UTC'
'''
# настроим статик и медиа
'''
STATIC_URL = 'static/' #чтобы поддерживать статические файлы (например, css)
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

MEDIA_URL = 'media/' # чтобы поддерживать медиа файлы
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
'''
# accounts, product, orders создаются по единому шаблону
# models - за связь с БД. В models.py есть уже import
# view - как будет отображаться
# admin - 

# далее создаем модель в models.py в папке accounts
# далее создаем модель в models.py в папке product

# в настройках указываем модель пользователя
'''
AUTH_USER_MODEL = 'название_приложения.НазваниеМодели' #'accounts.User'
'''

# далее создаем миграцию
'''python3 manage.py makemigrations'''

# и мигрируем данные
'''python3 manage.py migrate'''

# если все мигрировано успешно, запускаем сервер
'''python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 29, 2022 - 11:54:05
Django version 4.0.5, using settings 'shop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.'''

# переходим по ссылке http://127.0.0.1:8000/

# если миграция неправильная(что-то упустили и запустили миграцию), то 
# 1. удаляем БД и заново создаем
# 2. в модельках (accounts и product) в папке migrations удаляем документ 0001_initial.py
# 3. заново создаем миграцию и мигрируем данные

# после создания моделей, можно создать пользователей
# в терминале
'''python3 manage.py createsuperuser'''
# вводим email, пользователя и пароль (пропускаем проверку пароля - вводим '1' и на вопрос "пропустить?" выбираем 'y')
'''
Email: test_django@gmail.com
Name: test_user
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
'''
# запускаем сервер 
'''
python3 manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 30, 2022 - 10:53:26
Django version 4.0.5, using settings 'shop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
'''
# регистрируем юзера в admin.py в accounts
'''
from django.contrib.auth import get_user_model
User = get_user_model()
admin.site.register(User)
'''
# Регистрируем категории и продукты в admin.py в product
'''
from .models import Category, Product
admin.site.register(Category)
admin.site.register(Product)
'''
# переходим на сайт
# добавим категории и товары на сайте
'''
# если порт занят, то можно очистить порт (вместо 8000 может быть любой другой порт)
fuser -k 8000/tcp

# на MacOS:
lsof -i :8000 #определяет на каком порту мы сидим
# находим process id и
kill -9 pid # или
kill -9 $(lsof -ti :8000)
'''

# Создаем API для операций
# В product - views.py (отвечает за обработку запросов) пропишем функцию запросов (get), добавим сериалайзер, чтобы конвертировать данные в JSON

# Создадим serializers.py в папке product, где настроим поля.
# serializers отображает поля в нужном формате

# В папке shop в urls.py добавим созданную функцию

# Перейдем на сайт, в хостнейм укажем расширение /product/ и проверим

#ORM запросы:
# SELECT

# SELECT * FROM product;
'''Product.objects.all()'''

# SELECT name, price FROM product;
'''Product.objects.only('name', 'price')'''

# SELECT * FROM product WHERE condition;
'''Product.objects.filter(condition)'''
# condition types:
# COMPARISONS
# ==
# SELECT * FROM product WHERE category_id = 'tv';
'''Product.objects.filter(category_id='tv')'''
# !=
# SELECT * FROM product WHERE NOT category_id = 'tv';
'''Product.objects.filter(~Q(category_id='tv'))'''
'''Product.objects.exclude(category_id='tv')'''
# >
# SELECT * FROM product WHERE price > 30000;
'''Product.objects.filter(price__gt=30000)'''
# <
# SELECT * FROM product WHERE price < 30000;
'''Product.objects.filter(price__lt=30000)'''
# >=
# SELECT * FROM product WHERE price >= 30000;
'''Product.objects.filter(price__gte=30000)'''
# <=
# SELECT * FROM product WHERE price <= 30000;
'''Product.objects.filter(price__lte=30000)'''
# IN
# SELECT * FROM product WHERE category_id IN ('tv', 'smartphones');
'''Product.objects.filter(category_id__in=['tv', 'smartphones'])'''
# BETWEEN
# SELECT * FROM product WHERE price BETWEEN 40000 AND 50000;
'''Product.objects.filter(price__range=[40000, 50000])'''
# LIKE, ILIKE
'str'
# SELECT * FROM product WHERE name LIKE 'Apple Ihone 13';
'''Product.objects.filter(name__exact='Apple Ihone 13')'''
# SELECT * FROM product WHERE name ILIKE 'Apple Ihone 13';
'''Product.objects.filter(name__iexact='Apple Ihone 13')'''
'str%'
# SELECT * FROM product WHERE name LIKE 'Apple%';
'''Product.objects.filter(name__startswith='Apple')'''
# SELECT * FROM product WHERE name ILIKE 'Apple%';
'''Product.objects.filter(name__istartswith='Apple')'''
'%str'
# SELECT * FROM product WHERE name LIKE '%13';
'''Product.objects.filter(name__endsswith='13')'''
# SELECT * FROM product WHERE name ILIKE '%13';
'''Product.objects.filter(name__iendswith='13')'''
'%str%'
# SELECT * FROM product WHERE name LIKE '%Apple%';
'''Product.objects.filter(name__contains='Apple')'''
# SELECT * FROM product WHERE name ILIKE '%Apple%';
'''Product.objects.filter(name__icontains='Apple')'''

# ORDER BY
# SELECT * FROM product ORDER BY price ASC;
'''Product.objects.order_by('price')'''
# SELECT * FROM product ORDER BY price DESC;
'''Product.objects.order_by('-price')'''

# LIMIT
# SELECT * FROM product LIMIT 10;
'''Product.objects.all()[:10]'''
# SELECT * FROM product LIMIT 10 OFFSET 5;
'''Product.objects.all()[5:15]'''

# проект будет в гитхабе
# INSERT
# UPDATE
# DELETE







