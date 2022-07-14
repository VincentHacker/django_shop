from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.mail import send_mail

from accounts.tasks import send_activation_mail

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField(min_length=8)
    password_confirm = serializers.CharField(min_length=8)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Почта уже занята')
        return email

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')
        return super().validate(attrs)

    def create(self):
        user = User.objects.create_user(**self.validated_data) # имя, email и pswd - распаковали в словарь
        user.create_activation_code()
        # user.send_activation_code()
        send_activation_mail.delay(user.email, user.activation_code) # добавили для celery
        return user


# class ActivationSerializer(serializers.Serializer):
#     pass # не нужен пока. нужен был бы для кода активации

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользватель с указанным email не зарегистрирован')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')      
        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise serializers.ValidationError('Неверный пароль')
        return super().validate(attrs)


class RestorePasswordSerializer(serializers.Serializer): # когда забыл пароль
    email = serializers.EmailField() # вводим email
    # и нужно проверить, что email существует
    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользватель с указанным email не зарегистрирован')
        return email

    def send_verification_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email) # далее отправляется код верификации
        user.create_activation_code() #создаем код верификации
        #отправляем письмо с кодом верификации
        send_mail(
                'Восстановление пароля',
                f'Ваш код верификации: {user.activation_code}',
                'test_user@gmail.com', # здесь любая почта, т.к. она все равно поменяется
                [user.email]
        )

#для установления нового пароля
class RestorePasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField()
    activation_code = serializers.CharField(max_length=20, min_length=20)
    password = serializers.CharField(min_length=8)
    password_confirm = serializers.CharField(min_length=8)

    def validate(self, attrs):
        # print(attrs)
        email = attrs.get('email')
        code = attrs.get('activation_code')
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError('Пользватель не найден')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')
        return super().validate(attrs)
    # установим новый пароль
    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()

# когда знаешь, но хочешь поменять
class ChangePasswordSerializer(serializers.Serializer): 
    old_password = serializers.CharField(min_length=8) #ввод старого пароля
    password = serializers.CharField(min_length=8) #ввод нового пароля
    password_confirm = serializers.CharField(min_length=8) # подтверждение нового пароля
    
    # валидация старого пароля(чтобы чужой не смог поменять пароль)
    def validate_old_password(self, password):
        user = self.context['request'].user # напрямую получаем юзера
        if not user.check_password(password): # у юзера есть метод check_password, который шифрует и сравнивает с паролем в БД
            raise serializers.ValidationError('Неверный пароль')
        return password
    # подтверждаем новый пароль
    def validate(self, attrs):
        pass1 = attrs.get('password') # получим новую пароль
        pass2 = attrs.get('password_confirm') # и новую пароль для подтверждения
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')
        return super().validate(attrs)
    # устанавливаем новый пароль
    def set_new_password(self):
        user = self.context['request'].user
        password = self.validated_data.get('password') # validated_data работает как attrs. Данные берет из postman
        user.set_password(password)
        user.save()


