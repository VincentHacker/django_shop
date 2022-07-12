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
# проект будет в гитхабе

# Создаем API для операций
# В product - views.py (отвечает за обработку запросов) пропишем функцию запросов (get), добавим сериалайзер, чтобы конвертировать данные в JSON

# Создадим serializers.py в папке product, где настроим поля.
# serializers отображает поля в нужном формате

# В папке shop в urls.py добавим созданную функцию

# Перейдем на сайт, в хостнейм укажем расширение /product/ и проверим

# добавляем .gitignore, заходим на сайт gitignore.io, выбираем django, v


# Создадим репозиторий на гитхабе django_shop
'''
^C(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ git init
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ git remote add origin git@github.com:VincentHacker/django_shop.git
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ git add .
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ git commit -m 'Add project'
(env) atai@atai-Aspire-A315-55G:~/Desktop/Bootcamp/week8/py20_shop$ git push origin master
Enumerating objects: 36, done.
Counting objects: 100% (36/36), done.
Delta compression using up to 8 threads
Compressing objects: 100% (34/34), done.
Writing objects: 100% (36/36), 13.59 KiB | 1.04 MiB/s, done.
Total 36 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), done.
To github.com:VincentHacker/django_shop.git
 * [new branch]      master -> master
 '''

# добавим в serializer modelSerializer. Если есть моделька, можно выбрать данные, не прописывать

# добавим APIView (и ListAPIView - тогда image станет кликабельным) в view.py в product

# исправим urls.py
# и добавим импорты в urls.py
'''
from django.conf import settings
from django.conf.urls.static import static
'''
# crud классы имеются в generics.py (работает через mixins.py)

# postman - как API клиент. Можно отправлять данные на сервер

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

# INSERT-------------------------------------
# INSERT INTO product (...) VALUES (...);
'''Product.objects.create(name='...', description='...', и т.д.)'''
# можно также через экземлпяр класса и вызвав метод save:
'''
product = Product(name='...', description='...')
product.save()
'''
# INSERT INTO product (fields) VALUES (...), (...);
'''
Product.objects.bulk_create(
    [
        Product(...),
        Product(...)
        ]
)
'''
# UPDATE
# UPDATE product SET price = 50000;
'''Product.objects.update(price=50000)'''
# UPDATE product SET price = 50000 WHERE category_id = 'notebooks';
'''Product.objects.filter(category_id='notebooks').update(price=50000)'''

# DELETE
# DELETE FROM product;
'''Product.objects.delete()'''
# DELETE FROM product WHERE price > 50000;
'''Product.objects.filter(price__gt=50000).delete()'''

# получение одного объекта
''' Category.objects.get(slug='tv')'''
''' Product.objects.get()''' #запрос по уникальному полю, обычно по id
# Возможные ошибки:
# DoesNotExist - если не найдет
# MultipleObjectsReturned - если найдет несколько
# поэтому нужно прописывать так, чтобы находить только один объект

# количество записей
# SELECT COUNT(*) FROM product;
'''Product.objects.count()'''

# SELECT COUNT(*) FROM product WHERE price < 20000;
'''Product.objects.filter(price__lt=20000).count()'''

# про методы:
'''https://docs.djangoproject.com/en/4.0/ref/models/querysets/#queryset-api'''

# в постман создать workspace -> collections и добавить запросы (add requests): а) называем действие, б) выбираем метод и в) указываем путь к серверу
'''
Creating products
POST
http://127.0.0.1:8000/product/create/'''

'''
Listing products
GET
http://127.0.0.1:8000/product/'''

'''
View product details
GET
http://127.0.0.1:8000/product/1/'''

'''
Updating products
PATCH
http://127.0.0.1:8000/product/update/1/'''

'''
Removing products
DEL
http://127.0.0.1:8000/product/delete/2/'''

# запускаем сервер
# переходим в postman и нажимаем send по каждому действию. Для create, update, delete открываем body - form-data

# изменим views.py: объединим классы, а еще лучше добавим ModelViewSet. Также изменим шаблоны путей в urls.py (можно еще короче (т.е. правильно) сделать через router)

# переходим в postman и меняем пути согласно измененным шаблонам в urls.py

# почитать:
'''
https://www.django-rest-framework.org/api-guide/views/
https://www.django-rest-framework.org/api-guide/generic-views/
https://www.django-rest-framework.org/api-guide/viewsets/
https://www.django-rest-framework.org/api-guide/routers/
'''
# создаем новый файл urls.py в папке product и устанавливаем router

# в urls.py в папке shop прописываем путь

# заходим в оф сайт rest_framework, ищем pagination и копипастим в settings.py:
'''
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
'''
# фикчерс?

# на сайте rest framework ищем filter и копипастим в settings.py 
'''
'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
'''
# установим django-filter (добавляем в requirements.py)
'''pip install django-filter'''

# добавим 'django_filters' в installed apps в settings.py

# есть api, generics и vewсеты

# обновляем product/views.py

# создаем новый файл product/filter.py импортируем rest_framework и прописываем класс ProductPriceFilter, исправляем product/views.py

# добавим класс в product/admin.py ProductAdmin, установим декораторы и закомментируем вызов функций

# создадим код активации в accounts/models.py (для верификации пользователя)

# --settings 

# smptp ?

# СКРЫТИЕ ДАННЫХ:

# 1. создаем корневой файл .env.example (только для инструкции) и прописываем переменные с пустыми значениями:
'''
EMAIL_HOST = 
SMTP_HOST = 
EMAIL_PASSWORD = 
EMAIL_PORT = 
EMAIL_USE_TLS = 
'''
# 2. генерируем app password in google

# 3. создаем корневой файл .env и заполняем данные. В EMAIL_PASSWORD вставляем сгенерированный gmail пароль
'''
EMAIL_HOST = ataikasymbekov@gmail.com
SMTP_HOST = smtp.gmail.com
EMAIL_PASSWORD = zlonejntprsldkmj
EMAIL_PORT = 587
EMAIL_USE_TLS = True
'''
# 4. Устанавливаем python-decouple (и добавляем в requirements.txt)
'''
pip install python-decouple
'''
# 5. В файле shop/settings.py импортируем:
'''
from decouple import config
'''
# 6. В этом файле прописываем данные и скрываем ерез config:
'''
EMAIL_HOST = config('SMTP_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
'''

# добавляем serializers.py и urls.py в accounts
# добавляем классы в serializers.py

# добавляем классы в accounts/views.py

# прописываем пути в urls.py

# исправим в accounts/models.py
'''
activation_link = f'http://127.0.0.1:8000/account/activate/{self.activation_code}'
'''
# activate -> activation

# установим djangorestframework_simplejwt (добавим в requirements.txt) для логина
# добавим класс в serializers.py и пропишем login в account/views.py

# loginView не наследуется от APIView, т.к. есть специальный класс TokenObtainPairView. Прописываем этот класс к классу LoginView
# Заполняем данные в postman, генерируем временную почту и проверяем регистрацию и активацию аккаунта

# добавим в settings.py default_authentication_classes, где REST_FRAMEWORK и rest_framework_simplejwt в INSTALLED_APPS и 

# добавляем SIMPLE_SWT, импортируем timedelta

# Вводим email и password в postman где login и проверяем логин
# Кроме form data также в postman-raw выбрать JSON и ввести {"email": "email_name", "password": "password_name"}

# в accounts/serializers.py прописываем класс RestorePasswordSerializer для восстановления пароля

# в accounts/serializers.py прописываем класс RestorePasswordCompleteSerializer для создания нового пароля

# привязываем вьюшку в accounts/views.py

# привязываем accounts/urls.py

# реализуем остальные вьюшки (changepassword & logout)
# # в accounts/serializers.py прописываем класс ChangePasswordSerializer для изменения пароля

# привязываем вьюшку в accounts/views.py и urls

# сделаем logout в serializers.py -> views.py -> urls.py
# добавим еще класс UpdateTokenView во вьюшке


# Tima's lesson
# запрос - сеттингс middleware - 

# запрос - urls - view (попадает в request, data) - serializer (у serializers есть атрибут data - попадает в attrs(где словарь ordereddict с email и т.д.))  

# in views.py:
# print(type(request))
# print(request.headers)
# print(dict(data)['email'])

# set_password в models.py шифрует пароль


# с помощью тестов можно запустить автоматическое тестирование
# TDD проект. Бывает, пишут тесты а потом весь проект под тест

# Tima's lesson
# сегодня добавим permissions, comments и подключим swagger

# python3 manage.py --help

# created Makefile

# slug прописывали вручную. Можно сделать так, чтобы слаг подставлял сам, на основе name (имя переводится в латиницу в нижнем регистре)
# pip install python-slugify
# slug = models.SlugField(max_length=100, blank=True)
# добавить метод save

# зайти сразу в БД
# python3 manage.py dbshell

# --------------------------------------------
# ПОДКЛЮЧЕНИЕ ДОКУМЕНТАЦИИ SWAGGER

# инфо на сайте:
'''
https://drf-yasg.readthedocs.io/en/stable/readme.html
'''
# установим drf-yasg:
'''pip install wheel'''
'''pip install drf-yasg'''
# добавляем 3 импорта:
'''
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
'''
# добавляем параметры shema_view:
'''
schema_view = get_schema_view(
   openapi.Info(
      title="Py20 Shop",
      default_version='v1',
      description="This is our API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
'''
# добавляем в начало urlpatterns = [
'''
    path('swagger/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
'''
# -------------------------------------------

# Adilet's lesson

# пропишем модельки в orders/models.py и смигрируем данные

# создадим serializers.py и urls.py в orders

# TODO: Пройтись по всему проекту, проверить все запросы
# TODO: Подготовить проект к деплою
# TODO: Написать тесты
# Plan:
# TODO: FastAPI
# TODO: Docker
# TODO: Asynch
# TODO: pytest

# DEPLOY

# удалить окружение
# rm -rf venv/



## postgres://yyrgwvjovdbudf:7cc4d41f54cec5d621f3f36925bc74364df052f23f07ea5bc2f0a1e74fc4e995@ec2-3-217-14-181.compute-1.amazonaws.com:5432/d29335ei3o5qk8


# 127.0.0.1 localhost cryptic-tundra-91979.herokuapp.com