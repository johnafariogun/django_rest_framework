from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q


from base.models import Advocate
from .serializers import AdvocateSerializer
# Create your views here.
@api_view(['GET'])
def endpoints(request):

    data=['/advocates', 'advocates/:username']
    return Response(data)
    # return JsonResponse(data, safe = False)
    # safe = False allows us to receive other data types and not just dictionaries


@api_view(['GET',"POST"])
def advocate_list(request):
    # Handles GET requests
    if request.method == 'GET':
    # simple search functionality:
        query = request.GET.get('query')
        if query == None: # if there is npo query
            query = ''

        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(Bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many =True)
        return Response(serializer.data)


    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username = request.data['username'],
            Bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)


@api_view(['GET', "PUT","DELETE"])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username = username)
    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)

    
    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.Bio = request.data['bio']
        
        advocate.save()
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)


    if request.method == "DELETE":
        advocate.delete()
        
        return redirect('')

