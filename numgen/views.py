from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Token
from .models import Numbers
from .models import State
from .serializer import TokenSerializer
import random


# Create your views here.


@api_view(["GET"])
def confirm_token(request, token):
    # Check if the token exists in the database
    token_exists = Token.objects.filter(key=token).exists()

    if token_exists:
        # If the token exists, serialize the data (assuming no specific serialization needed here)
        token_obj = Token.objects.get(key=token)
        serializer = TokenSerializer(token_obj)
        
        # Return the serialized data with a 200 OK status
        return Response({'Success': serializer.data}, status=status.HTTP_200_OK)
    else:
        # If the token does not exist, return a 403 Forbidden status
        return Response({'detail': 'Invalid token'}, status=status.HTTP_403_FORBIDDEN)
    


@api_view(["GET"])
def get_random_number(request, state_name):
    try:
        # Retrieve the state based on the provided state name
        state = State.objects.get(state=state_name)
        
        # Get all numbers associated with the state
        numbers = Numbers.objects.filter(stat=state)
        
        if not numbers.exists():
            # If no numbers are found, return a 404 status
            return Response({'detail': 'No numbers found for this state'}, status=status.HTTP_404_NOT_FOUND)
        
        # Choose one random number from the list
        random_number = random.choice(numbers).num
        
        # Return the random number
        return Response({'random_number': random_number}, status=status.HTTP_200_OK)
    
    except State.DoesNotExist:
        # If the state doesn't exist, return a 404 Not Found status
        return Response({'detail': state}, status=status.HTTP_404_NOT_FOUND)