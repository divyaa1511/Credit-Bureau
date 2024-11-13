from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, UserResponse


@login_required
def question_form(request):
    questions = Question.objects.all()

    questions_data = [{
        'id': question.id,
        'text': question.text,
        'answer_a': question.answer_a,
        'answer_b': question.answer_b,
        'answer_c': question.answer_c,
        'answer_d': question.answer_d,
    } for question in questions]

    if request.method == 'POST':
        total_score = 0
        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            if answer:
                UserResponse.objects.create(
                    user=request.user,
                    question=question,
                    answer=answer
                )
                if answer == 'A':
                    total_score += question.score_a
                elif answer == 'B':
                    total_score += question.score_b
                elif answer == 'C':
                    total_score += question.score_c
                elif answer == 'D':
                    total_score += question.score_d
        request.session['total_score'] = total_score
        return redirect('results')

    return render(request, 'questions/question_form.html', {'questions': questions_data}) # noqa


@login_required
def results_view(request):
    # Retrieve score from session
    score = request.session.get('total_score', 0)

    return render(request, 'questions/results.html', {'score': score})
