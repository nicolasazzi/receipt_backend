from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer, LoginInfoSerializer
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


@api_view(['POST',])
@permission_classes([AllowAny])
def login_view(request):

    phone = request.data['phone_number']
    password = request.data['password']
    try:
        account = Account.objects.get(phone_number=phone)
        if not account.check_password(password):
            print('entered')
            raise Exception()

        serializer = LoginInfoSerializer(account)
        token = Token.objects.get(user=account).key

        data = serializer.data
        data['token'] = token
        
        return Response(data, status=200)
    except Exception as e:
        return Response({'response': str(e)}, status=404)

