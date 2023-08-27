from django.forms import ModelForm
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['pub_date', 'question_text']
