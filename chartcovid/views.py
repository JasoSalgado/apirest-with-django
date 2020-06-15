from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Country
from .serializers import CountrySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


   


class GenericAPIView(generics.GenericAPIView, 
                    mixins.ListModelMixin, 
                    mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    # Fixing url 
    
    lookup_field = 'id'

    # Adding authentication to the API
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

        return self.list(request)

    
    def post(self, request):
        return self.create(request)


    def put(self, request, id=None):
        return self.update(request, id)

    
    def delete(self, request, id):
        return self.destroy(request, id)



class CountryAPIView(APIView):
    
    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many = True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = CountrySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CountryDetails(APIView):

    def get_object(self, id):
        try:
            return Country.object.get(id = id)

        except Country.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    

    def get(self, request, id):
        country = self.get_object(id)
        serializer = CountrySerializer(country)
        return Response(serializer.data)


    def put(self, request, id):
        country = self.get_object(id)
        serializer = CountrySerializer(country, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        country = self.get_object(id)
        country.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CountrySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def country_detail(request, pk):
    try:
        country = Country.object.get(pk = pk)
    except Country.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CountrySerializer(country, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        country.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
