from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Token
from .models import State,StateCode, Phrases
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
def generate_phone_numbers(request):
    phone_numbers = set()  # Use a set to avoid duplicates

    while len(phone_numbers) < 20:
        # Randomly select a state code
        state_code = random.choice(StateCode.objects.all())
        
        # Get all phrases associated with the selected state code
        phrases = Phrases.objects.filter(origin=state_code)

        # Randomly select one phrase from the list
        if phrases.exists():
            phrase = random.choice(phrases)
        else:
            return Response({'detail': 'No phrases found for the selected state code'}, status=status.HTTP_404_NOT_FOUND)

        # Generate the first 6 digits from state code and phrase code
        first_six_digits = f"{state_code.code}{phrase.code}"

        # Generate a random 5-digit number to complete the 11-digit phone number
        last_five_digits = random.randint(10000, 99999)

        # Form the complete phone number
        full_phone_number = f"{first_six_digits}{last_five_digits}"

        # Add the phone number to the set to ensure uniqueness
        phone_numbers.add(full_phone_number)

    return Response({'phone_numbers': list(phone_numbers)}, status=status.HTTP_200_OK)