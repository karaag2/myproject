from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from social_django.utils import psa
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from api.models import Note
from api.serializers import NoteSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
@psa('social:complete')
def register_by_access_token(request):
    token = request.data.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        return Response({
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
    else:
        return Response('Error', status=400)
class ManualTestView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request):
        return Response("Manual test endpoint is working!")