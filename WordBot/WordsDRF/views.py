
from .models import Words

from rest_framework.response import Response
from .serializers import WordSerializer
from rest_framework import viewsets



class WordAPIList(viewsets.ModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordSerializer


class WordAPIcategoryStreet(viewsets.ReadOnlyModelViewSet):
    queryset = Words.objects.filter(catagory=3)
    serializer_class = WordSerializer

class WordAPIcategoryHome(viewsets.ReadOnlyModelViewSet):
    queryset = Words.objects.filter(catagory=2)
    serializer_class = WordSerializer

class WordAPIcategoryFood(viewsets.ReadOnlyModelViewSet):
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
