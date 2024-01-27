from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema

from api.serializers import LoginSerializer

@extend_schema(
    request=LoginSerializer, 
    responses={200: {'description': 'Action successful'}}, 
)
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({"status": status.HTTP_200_OK, "token": str(refresh.access_token)})