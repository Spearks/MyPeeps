from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from api.models import PeepsMetric
from api.serializers import ActionSerializer, PeepsSerializer
from api.permissions import PeepsUserPermissions

from mypeeps.settings import ACTIONS
actions = ACTIONS

def apply_effect(UserOption):
    pass

# TODO: User auth, Rate-limit, history 
@extend_schema(
    request=ActionSerializer, 
    responses={200: {'description': 'Action successful'}}, 
)
class ActionsPeepView(APIView):
    permission_classes = [IsAuthenticated, PeepsUserPermissions]  

    def post(self, request):
        
        serializer = ActionSerializer(data=request.data, context={'action_name' : self.request.data.get("name", None)})

        if serializer.is_valid():

            selected_action = actions[serializer.validated_data["name"]]
            peep = serializer.validated_data["peep"]
            useroption = selected_action["UserOptions"][serializer.validated_data["options"]["name"]]
            
            peep.add_to_attribute("romance", +2.2)
            peep.save()


            metric = PeepsMetric()
            metric.action = serializer.validated_data["options"]["name"] # 
            metric.peep = peep
            metric.attribute_hp = peep.attribute_hp
            metric.attribute_creativity = peep.attribute_creativity
            metric.attribute_romance = peep.attribute_romance

            metric.save()


            peep_serialized = PeepsSerializer(peep) 

            message_serialized = {
                "message" : "Successful action",
                "data" : peep_serialized.data
            }
            return Response(message_serialized)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)