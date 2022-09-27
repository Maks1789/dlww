from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question

# Create your views here.
class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
