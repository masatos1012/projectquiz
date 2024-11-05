from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.question_view, name='question'),
    path('result/', views.result_view, name='result'),
    path('reset_session/', views.reset_session_view, name='reset_session'),  # 新しいパスを追加
]
