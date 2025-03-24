from django.urls import path
from .views import question_list, question_detail, ask_question

urlpatterns = [
    path('', question_list, name='question_list'),
    path('question/<int:pk>/', question_detail, name='question_detail'),
    path('ask/', ask_question, name='ask_question'),
]
