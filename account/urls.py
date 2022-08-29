from django.urls import path, include
from account.views import ChangePasswordView

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('update/', views.update, name="update"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
]
