from rest_framework import serializers
from .models import Interleaver

class InterleaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interleaver
        fields = ('id', 'title', 'description', 'completed')