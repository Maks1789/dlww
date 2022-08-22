from rest_framework import serializers
from . import models

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = "__all__"
