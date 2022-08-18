from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WordSerializer
from . import models
from django.http import HttpResponseNotFound


class NextWord (APIView):
    def get (self, request, pk, format=None):
        word = models.Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound()
        ser_word = WordSerializer(word, many=False)
        return Response(ser_word.data)
