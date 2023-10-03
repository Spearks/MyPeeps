from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Peeps
from drf_spectacular.utils import extend_schema
from rest_framework import serializers

class ActionsPeepSerializer(serializers.Serializer):
    action = serializers.CharField(max_length=100)

    def validate(self, data):
        action = data.get('action')

        allowed_actions = ['action1', 'action2', 'action3']

        if action not in allowed_actions:
            raise serializers.ValidationError({'action': 'Invalid action. Allowed actions are action1, action2, action3.'})

        return data



@extend_schema(
    request=ActionsPeepSerializer, 
    responses={200: {'description': 'Action successful'}}, 
)
class ActionsPeepView(APIView):
    
    def post(self, request):

        serializer = ActionsPeepSerializer(data=request.data)

        if serializer.is_valid():

            action = serializer.validated_data['action']

            return Response({'message': f'Successful action: {action}'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)