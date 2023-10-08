from rest_framework import viewsets
from api.models import Peeps
from api.serializers import PeepsSerializer
from cacheops import cache

class PeepsView(viewsets.ModelViewSet):
    """
    API endopoint to fetch all Peeps objects.
    """

    queryset = Peeps.objects.all().order_by('-created_at').cache()

    serializer_class = PeepsSerializer