from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MultiplicationQuestion, UserProgress
import random
from datetime import datetime, timedelta
import json

def get_next_question(user, operation_type="multiplication"):
    """
    Seçilen işlem türüne göre soru üret
    Generate question based on selected operation type
    """
    if operation_type == "multiplication":
        # Çarpma işlemi için 1-9 arası sayılar
        number1 = random.randint(1, 9)
        number2 = random.randint(1, 9)
    elif operation_type == "division":
        # Bölme işlemi için tam bölünen sayılar
        divisor = random.randint(2, 9)
        result = random.randint(1, 9)
        number1 = divisor * result
        number2 = divisor
    elif operation_type == "addition":
        # Toplama işlemi için 0-9 arası
        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)
    else:  # subtraction
        # Çıkarma işlemi için pozitif sonuç verecek sayılar
        number1 = random.randint(1, 9)
        number2 = random.randint(0, number1)
    
    return {
        'number1': number1,
        'number2': number2,
        'operation': operation_type  # İşlem türünü geri gönder
    }

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
    operation_type = request.GET.get('operation', 'multiplication')
    question = get_next_question(request.user, operation_type)
    
    if isinstance(question, MultiplicationQuestion):
        return JsonResponse({
            'number1': question.number1,
            'number2': question.number2,
            'operation': 'multiplication',
            'id': question.id
        })
    else:
        return JsonResponse(question)

@login_required
def check_answer(request):
    """
    AJAX ile cevap kontrolü
    Check answer via AJAX
    """
    try:
        data = json.loads(request.body)
        operation = data.get('operation', 'multiplication')
        user_answer = int(data.get('answer'))
        number1 = int(data.get('number1'))
        number2 = int(data.get('number2'))
        
        # İşleme göre doğru cevabı hesapla
        if operation == 'multiplication':
            correct_answer = number1 * number2
        elif operation == 'division':
            correct_answer = int(number1 / number2)  # Tam sayı bölme sonucu
        elif operation == 'addition':
            correct_answer = number1 + number2
        else:  # subtraction
            correct_answer = number1 - number2
        
        # Debug bilgisi ekle
        debug_info = {
            'correct': user_answer == correct_answer,
            'correct_answer': correct_answer,
            'user_answer': user_answer,
            'operation': operation,
            'number1': number1,
            'number2': number2
        }
        
        return JsonResponse(debug_info)
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)
