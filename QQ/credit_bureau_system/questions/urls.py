from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.question_form, name='question_form'),
    path('results/', views.results_view, name='results'),
]
