from django.core.management.base import BaseCommand
from core.models import MultiplicationQuestion

class Command(BaseCommand):
    help = 'Çarpım tablosu sorularını oluşturur / Creates multiplication table questions'

    def handle(self, *args, **kwargs):
        # Mevcut soruları temizle / Clear existing questions
        MultiplicationQuestion.objects.all().delete()
        
        # 2'den 9'a kadar olan çarpımlar / Multiplications from 2 to 9
        for i in range(2, 10):
            for j in range(i, 10):  # Çin yöntemi: sadece köşegenin üstü / Chinese method: only above diagonal
                question = MultiplicationQuestion(
                    number1=i,
                    number2=j,
                    difficulty=1
                )
                question.save()
                
                self.stdout.write(
                    self.style.SUCCESS(f'Soru oluşturuldu / Question created: {i} x {j}')
                ) 