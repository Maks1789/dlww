from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Words

from rest_framework.response import Response
from .serializers import WordSerializer
from . import models
from django.http import HttpResponseNotFound


class WordAPIList(generics.ListCreateAPIView):
    queryset = Words.objects.all()
    serializer_class = WordSerializer


class WordAPIcategoryStreet(generics.ListCreateAPIView):
    queryset = Words.objects.filter(catagory=3)
    serializer_class = WordSerializer

class WordAPIcategoryHome(generics.ListCreateAPIView):
    queryset = Words.objects.filter(catagory=2)
    serializer_class = WordSerializer

class WordAPIcategoryFood(generics.ListCreateAPIView):
    queryset = Words.objects.filter(catagory=1)
    serializer_class = WordSerializer



''''  
class NextWord (APIView):
    def get (self, request, pk, format=None):
        word = models.Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound()
        ser_word = WordSerializer(word, many=False)
        return Response(ser_word.data)
'''
