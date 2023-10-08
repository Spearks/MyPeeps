from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from api.models import PeepsMetric
from api.serializers import ActionSerializer, PeepsSerializer
from api.permissions import PeepsUserPermissions

from mypeeps.settings import ACTIONS

from django.utils import timezone
from datetime import timedelta

from types import NoneType

actions = ACTIONS

# TODO: Split in functions to be more readable
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
                
            current_time = timezone.now()
            # Check if Peep is in throttling 
            last_metric = PeepsMetric.objects.all().cache().filter(peep=peep, action=serializer.validated_data["options"]["name"]).last()
        
            rate_limit_threshold = current_time - timedelta(minutes=selected_action["Ratelimit"]["minute"])

            if type(last_metric) != NoneType and last_metric.time > rate_limit_threshold:
                message = {
                    "message" : "Action are in throttle-limited"
                }
                return Response(message)
            
            peep.add_to_attribute("romance", +2.2)
            peep.save()

            # Save to metrics
            metric = PeepsMetric()
            metric.action = serializer.validated_data["options"]["name"] 
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