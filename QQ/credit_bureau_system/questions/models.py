from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    answer_a = models.CharField(max_length=255)
    answer_b = models.CharField(max_length=255)
    answer_c = models.CharField(max_length=255)
    answer_d = models.CharField(max_length=255)
    score_a = models.IntegerField(default=0)
    score_b = models.IntegerField(default=0)
    score_c = models.IntegerField(default=0)
    score_d = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)  # 'A', 'B', 'C', or 'D'

    def get_score(self):
        if self.answer == 'A':
            return self.question.score_a
        elif self.answer == 'B':
            return self.question.score_b
        elif self.answer == 'C':
            return self.question.score_c
        elif self.answer == 'D':
            return self.question.score_d
        return 0
