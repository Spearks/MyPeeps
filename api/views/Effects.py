from rest_framework.response import Response
from rest_framework import status, viewsets

from django.utils import timezone

from api.serializers import EffectSerializer
from api.models import Effect

from drf_spectacular.utils import extend_schema

@extend_schema(
    request=EffectSerializer, 
    responses={200: {'description': 'Action successful'}}, 
)
class EffectViewSet(viewsets.GenericViewSet):

    def list(self, request):
        pass

    def retrieve(self, request, pk=None):
        try:
            current_time = timezone.localtime()

            effects = Effect.objects.filter(peep=pk, start_time__lte=current_time, end_time__gte=current_time)
            serializer = EffectSerializer(effects, many=True)

            Effect.objects.filter(peep=pk, end_time__lt=current_time).delete()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except EffectSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)