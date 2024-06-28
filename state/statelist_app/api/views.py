from rest_framework.response import Response
from statelist_app.models import Property, Company
from statelist_app.api.serializers import PropertySerializer, CompanySerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class CompanyAV(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=CompanySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertyListAV(APIView):

    def get(self, request):
        state = Property.objects.all()
        serializer = PropertySerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetailAV(APIView):
    def get(self, request, id):
        try:
            property = Property.objects.get(pk=id)

        except Property.DoesNotExist:
            return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            property = Property.objects.get(pk=id)
        except Property.DoesNotExist:
            return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            property = Property.objects.get(pk=id)
        except Property.DoesNotExist:
            return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

        property.delete()
        return Response({'message': 'El inmueble ha sido eliminado'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def property_list(request):
#     if request.method == 'GET':
#         state = Property.objects.all()
#         serializer = PropertySerializer(state, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         de_serializer = PropertySerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data, status=201)
#         else:
#             return Response(de_serializer.errors, status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def property_detail(request, id):
#     if request.method == 'GET':
#         try:
#             property = Property.objects.get(pk=id)
#             serializer = PropertySerializer(property)
#             return Response(serializer.data)
#         except Property.DoesNotExist:
#             return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         property = Property.objects.get(pk=id)
#         de_serializer = PropertySerializer(property, data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         try:
#             property = Property.objects.get(pk=id)
#             property.delete()
#         except Property.DoesNotExist:
#             return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

#         return Response(status=status.HTTP_204_NO_CONTENT)
