from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

from drf_spectacular.utils import extend_schema

from api.models import Peeps
from api.serializers import ActionSerializer

@extend_schema(
    request=ActionSerializer, 
    responses={200: {'description': 'Action successful'}}, 
)
class ActionsPeepView(APIView):
    
    def post(self, request):
        
        serializer = ActionSerializer(data=request.data, context={'action_name' : self.request.data.get("name", None)})

        if serializer.is_valid():

            #action = serializer.validated_data['action']
        
            return Response({'message': f'Successful action: '}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)