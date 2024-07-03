from django.urls import path

import user.views

urlpatterns = [
    path('', user.views.user_page),
    path('register', user.views.user_register),
    path('login', user.views.user_login),
]