from django.urls import path
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('signup/', signup_view, name='account_signup'),
    path('login/', login_view, name='account_login'),
    path('logout/', logout_view, name='account_logout'),  # 名前を指定
]
