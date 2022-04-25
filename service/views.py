from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from service.serializers import VendorSerializer
from rest_framework import status

from .models import Vendor


# Create your views here.

@api_view(['POST', 'OPTIONS'])
def insert_vendor(request):
    if isinstance(request.data, list):
        for obj in request.data:
            serializers = VendorSerializer(data=obj)
            if serializers.is_valid():
                serializers.save()
        return Response({'Status': 'Added List Of Objects'}, status=status.HTTP_200_OK)

    serializers = VendorSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'Status': 'Added'}, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'OPTIONS'])
def find_vendor(request):
    vendor = Vendor.objects.filter(mac=request.data['mac'])
    serializer = VendorSerializer(vendor, many=True)
    return Response(serializer.data)
