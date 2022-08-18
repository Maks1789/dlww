from rest_framework import serializers
from . import models

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Words
        fields = ('pk', 'gender', 'word', 'wordClass')
