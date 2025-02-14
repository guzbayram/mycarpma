from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MultiplicationQuestion, UserProgress
import random
from datetime import datetime, timedelta

def get_next_question(user):
    """
    Anki algoritmasına göre bir sonraki soruyu seç
    Select next question based on Anki algorithm
    """
    # Yanlış cevaplanan sorulara öncelik ver / Prioritize wrong answers
    wrong_questions = UserProgress.objects.filter(
        user=user,
        wrong_count__gt=0
    ).order_by('-wrong_count')
    
    if wrong_questions.exists():
        return wrong_questions.first().question
    
    # Yeni veya az görülen soruları seç / Select new or less seen questions
    questions = MultiplicationQuestion.objects.all()
    return random.choice(questions)

def home(request):
    """
    Ana sayfa görünümü
    Home page view
    """
    return render(request, 'core/home.html')

@login_required
def practice(request):
    """
    Alıştırma sayfası görünümü
    Practice page view
    """
    return render(request, 'core/practice.html')

@login_required
def get_question(request):
    """
    AJAX ile yeni soru al
    Get new question via AJAX
    """
    question = get_next_question(request.user)
    return JsonResponse({
        'number1': question.number1,
        'number2': question.number2,
        'id': question.id
    })

@login_required
def check_answer(request):
    """
    AJAX ile cevap kontrolü
    Check answer via AJAX
    """
    question_id = request.POST.get('question_id')
    user_answer = request.POST.get('answer')
    
    question = MultiplicationQuestion.objects.get(id=question_id)
    correct_answer = question.number1 * question.number2
    
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        question=question
    )
    
    is_correct = int(user_answer) == correct_answer
    
    if is_correct:
        progress.correct_count += 1
        # Doğru cevap için bir sonraki tekrar süresini artır
        # Increase next review time for correct answer
        progress.next_review = datetime.now() + timedelta(days=progress.correct_count)
    else:
        progress.wrong_count += 1
        # Yanlış cevap için hemen tekrar göster
        # Show immediately for wrong answer
        progress.next_review = datetime.now()
    
    progress.save()
    
    return JsonResponse({
        'correct': is_correct,
        'correct_answer': correct_answer
    })
