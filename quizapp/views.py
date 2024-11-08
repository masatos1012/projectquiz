from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Question, UserAnswer


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.first()  # 例として最初の質問を渡す
        return context


from django.utils import timezone


def question_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    total_questions = Question.objects.count()  # 登録されている問題数を取得
    next_pk = pk + 1  # 次の問題のpkを計算
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
        request.session['started_at'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')  # セッションの開始時刻を設定

    if 'started_at' not in request.session:
        request.session['started_at'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')  # セッションの開始時刻を設定

    request.session['last_activity_at'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')  # 最終アクティビティ時刻を更新

    if request.method == 'POST':
        selected_option = request.POST.get('answer')
        is_correct = (selected_option == question.correct_option)

        # ユーザーの回答を保存
        UserAnswer.objects.create(
            session_key=session_key,
            question=question,
            selected_option=selected_option,
            is_correct=is_correct
        )

        # 全ての問題を解答したか確認
        if UserAnswer.objects.filter(session_key=session_key).count() >= total_questions:
            return redirect('quiz:result')

        context = {
            'question': question,
            'selected_option': selected_option,
            'is_correct': is_correct,
            'next_pk': next_pk,
        }
        return render(request, 'answer.html', context)
    else:
        # 次の問題が存在するか確認
        if pk > total_questions:
            return redirect('quiz:result')

        context = {
            'question': question,
            'question_text': question.question_text,
            'option1': question.option1,
            'option2': question.option2,
            'option3': question.option3,
            'option4': question.option4,
            'correct_option': question.correct_option,
            'explanation': question.explanation,
            'next_pk': next_pk,
        }
        return render(request, 'question.html', context)


def result_view(request):
    session_key = request.session.session_key
    user_answers = UserAnswer.objects.filter(session_key=session_key)
    total_score = user_answers.filter(is_correct=True).count()

    # セッションの開始時刻と最終アクティビティ時刻を取得
    started_at = request.session.get('started_at')
    last_activity_at = request.session.get('last_activity_at')

    context = {
        'user_answers': user_answers,
        'total_score': total_score,
        'started_at': started_at,
        'last_activity_at': last_activity_at,
    }
    return render(request, 'result.html', context)


def reset_session_view(request):
    session_key = request.session.session_key
    if session_key:
        UserAnswer.objects.filter(session_key=session_key).delete()
    return redirect('quiz:index')
