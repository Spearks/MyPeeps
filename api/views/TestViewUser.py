from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateTestUserView(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=username + '@example.com'
        )

        return Response({
            'user_id': user.id
        })