from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['question_fild', 'answer']
