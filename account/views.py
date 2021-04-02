from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer
from .models import Account

@api_view(['POST',])
@permission_classes([AllowAny])
def registration_view(request):

    serializer = RegistrationSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'Successfully registered!'

        token = Token.objects.get(user=account).key
        data['token'] = token

    else:
        data = serializer.errors
    
    return Response(data)

@api_view(['POST',])
@permission_classes([AllowAny])
def check_phone_view(request):

    phone = request.data['phone']

    try:
        Account.objects.get(phone_number=phone)
        return Response({'allowed': False,})
    except:
        return Response({'allowed': True,})