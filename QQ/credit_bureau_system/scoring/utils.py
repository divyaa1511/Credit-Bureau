# scoring/utils.py
from questions.models import UserResponse


def calculate_credit_score(user):
    responses = UserResponse.objects.filter(user=user)
    total_score = 0
    for response in responses:
        total_score += response.get_score()
    return total_score
