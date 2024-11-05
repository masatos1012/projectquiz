from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.TextField(verbose_name="問題文", default="default_question_text")
    option1 = models.CharField(max_length=255, verbose_name="選択肢1", default="default_option1")
    option2 = models.CharField(max_length=255, verbose_name="選択肢2", default="default_option2")
    option3 = models.CharField(max_length=255, verbose_name="選択肢3", default="default_option3")
    option4 = models.CharField(max_length=255, verbose_name="選択肢4", default="default_option4")
    correct_option = models.CharField(max_length=255, verbose_name="正解の選択肢", default="option1")
    explanation = models.TextField(verbose_name="解説")


class UserAnswer(models.Model):
    session_key = models.CharField(max_length=40, verbose_name="セッションキー", default="default_session_key")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="問題", default=1)
    selected_option = models.CharField(max_length=255, verbose_name="選択肢", default="")
    is_correct = models.BooleanField(verbose_name="正解かどうか", default=False)
    answered_at = models.DateTimeField(default=timezone.now, verbose_name="回答日時")


# class Session(models.Model):
#     session_key = models.CharField(max_length=255, verbose_name="セッションキー", unique=True, default="default_session_key")
#     current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, verbose_name="現在の問題ID",
#                                          default=1)
#     started_at = models.DateTimeField(auto_now_add=True, verbose_name="セッション開始日時")
#     last_activity_at = models.DateTimeField(auto_now=True, verbose_name="最終アクティビティ日時")
