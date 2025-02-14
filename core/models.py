from django.db import models
from django.contrib.auth.models import User

class MultiplicationQuestion(models.Model):
    """
    Çarpım soruları için model
    Multiplication questions model
    """
    number1 = models.IntegerField()  # İlk sayı / First number
    number2 = models.IntegerField()  # İkinci sayı / Second number
    difficulty = models.IntegerField(default=1)  # Zorluk seviyesi / Difficulty level
    
    def __str__(self):
        return f"{self.number1} x {self.number2}"

class UserProgress(models.Model):
    """
    Kullanıcı ilerleme takibi için model
    User progress tracking model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(MultiplicationQuestion, on_delete=models.CASCADE)
    correct_count = models.IntegerField(default=0)  # Doğru cevap sayısı / Correct answer count
    wrong_count = models.IntegerField(default=0)  # Yanlış cevap sayısı / Wrong answer count
    last_seen = models.DateTimeField(auto_now=True)  # Son görülme tarihi / Last seen date
    next_review = models.DateTimeField(null=True)  # Bir sonraki tekrar tarihi / Next review date
    
    class Meta:
        unique_together = ['user', 'question']
