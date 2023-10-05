from rest_framework import serializers
import xml.etree.ElementTree as ET
from mypeeps.settings import BASE_DIR
import os

tree = ET.parse( os.path.join(BASE_DIR, "playbooks", "Actions.xml") )
root = tree.getroot()

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

        user_options = []
        for action in root.findall('Action'):

            if action.find("Name").text.strip() == action_name:
                options = action.find('UserOptions')
                if options is not None:
                    for option in options.findall('Option'):
                        option_name = option.find('Name').text.strip()
                        user_options.append(option_name)
                else:
                    return True
        return user_options

class ActionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    options = UserOptionsSerializer(many=False, context={"action_name" : name}, required=False)

    def validate_name(self, value):
        allowed_actions = [action.find('Name').text.strip() for action in root.findall('Action')]
        if value not in allowed_actions:
            raise serializers.ValidationError('Invalid Action. This action is not present in the Playbooks.')
        return value
