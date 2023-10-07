from rest_framework import serializers
from api.models import Peeps
from mypeeps.settings import ACTIONS
import os

actions = ACTIONS

class UserOptionsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def validate_name(self, value):
        action_name = self.context.get('action_name')

        allowed_options = self.get_user_options(action_name)
        if allowed_options == True: 
            return value
        
        if value not in allowed_options:
            raise serializers.ValidationError('Invalid UserOption. This option is not present in the Playbooks.')
        return value

    def get_user_options(self, action_name):

        allowed_user_options = actions[action_name]["UserOptions"].keys()

        if allowed_user_options is not None: 
            return allowed_user_options
        else: return True

class ActionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    options = UserOptionsSerializer(many=False, context={"action_name" : name}, required=False)
    peep = serializers.PrimaryKeyRelatedField(queryset=Peeps.objects.all())

    def validate_name(self, value):
        allowed_actions = actions.keys()
        if value not in allowed_actions:
            raise serializers.ValidationError('Invalid Action. This action is not present in the Playbooks.')
        return value
