from django.contrib import admin

from .models import Question, UserAnswer
''', Session'''


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_option')
    search_fields = ('question_text',)


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'answered_at')
    search_fields = ('session_key', 'answered_at')


# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     list_display = ('session_key', 'current_question', 'started_at', 'last_activity_at')
#     search_fields = ('session_key', 'current_question__question_text')
