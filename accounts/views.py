from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializers import RegistrationSerializer, LoginSerializer

from django.http import Http404

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import (RegistrationSerializer, LoginSerializer, RestorePasswordSerializer, RestorePasswordCompleteSerializer, ChangePasswordSerializer)

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenRefreshSerializer


User = get_user_model()


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            return Response('Регистрация прошла успешно')


class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Аккаунт успешно активирован!')
        except User.DoesNotExist:
            raise Http404


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UpdateTokenView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # token = request.data['refresh_token'] # лучше с сериалайзером, чтобы не делать все проверки в скобках
        token = request.data.get('refresh_token')
        if token is not None:
            token_obj = RefreshToken(token)
            token_obj.blacklist()
            return Response('Вы успешно разлогинились')
        else:
            return Response('Refresh токен обязателен', status=400)


class RestorePasswordView(APIView):
    def post(self, request):
        data = request.data # запрашивает данные
        serializer = RestorePasswordSerializer(data=data) # прогоняем через сериалайзер RestorePasswordSerializer
        # проверяем валидные ли данные
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_code()
            return Response('Вам выслан код верификации') # с фронтом договориться какой код выдать, сделать список кодов


class RestorePasswordCompleteView(APIView):
    def post(self, request):
        data = request.data # вытаскиваем data из реквеста
        serializer = RestorePasswordCompleteSerializer(data=data) # прогоняем через сериалайзер RestorePasswordCompleteSerializer
        # проверяем валидные ли данные
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлен')



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated] # IsAuthenticated будет требовать токен, поэтому передадим функцией токен

    def post(self, request):
        data = request.data
        serializer = ChangePasswordSerializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлен')