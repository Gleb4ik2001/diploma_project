from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import JobSeekerRegistrationSerializer
from rest_framework.permissions import AllowAny

class JobseekerRegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = JobSeekerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user_id': user.id, 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
