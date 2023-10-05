import os
import xml.etree.ElementTree as ET

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from api.models import Peeps
from api.serializers import ActionSerializer
from api.permissions import PeepsUserPermissions

from mypeeps.settings import BASE_DIR

tree = ET.parse( os.path.join(BASE_DIR, "playbooks", "Actions.xml") )
root = tree.getroot()

# TODO: User auth
@extend_schema(
    request=ActionSerializer, 
    responses={200: {'description': 'Action successful'}}, 
)
class ActionsPeepView(APIView):
    permission_classes = [IsAuthenticated, PeepsUserPermissions]  
    
    def post(self, request):
        
        serializer = ActionSerializer(data=request.data, context={'action_name' : self.request.data.get("name", None)})

        if serializer.is_valid():

            action = serializer.validated_data["name"]
            peep = serializer.validated_data["peep"]

            return Response({'message': f'Successful action: '}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)