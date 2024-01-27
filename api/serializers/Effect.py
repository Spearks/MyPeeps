from rest_framework import serializers
from api.models import Effect

class EffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effect
        fields = '__all__'