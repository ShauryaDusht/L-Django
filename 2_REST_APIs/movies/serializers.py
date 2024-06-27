from rest_framework import serializers
from .models import Moviedata

class MoviedataSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Moviedata
        fields = '__all__'