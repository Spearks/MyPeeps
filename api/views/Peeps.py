from rest_framework import viewsets
from api.models import Peeps, PeepsSerializer

class PeepsView(viewsets.ModelViewSet):
    """
    API endopoint to fetch all Peeps objects.
    """

    queryset = Peeps.objects.all().order_by('-created_at')

    serializer_class = PeepsSerializer