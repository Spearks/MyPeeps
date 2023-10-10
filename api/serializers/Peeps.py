from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from api.models import Peeps

class RelatedFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peeps
        fields = ['attribute_creativity', 'attribute_romance', 'attribute_hp']  

class PeepsSerializer(serializers.ModelSerializer):
    attributes = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_attributes(self, obj): 
        related_fields_data = RelatedFieldsSerializer(obj).data
        return {key.replace('attribute_', ''): value for key, value in related_fields_data.items() if key.startswith('attribute_')}

    class Meta:
        model = Peeps
        fields = ['id', 'name', 'created_at', 'seed', 'age', 'attributes','users']
