from rest_framework.response import Response
from statelist_app.models import Edification, Company
from statelist_app.api.serializers import EdificationSerializer, CompanySerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class CompanyAV(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(
            companies, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAV(APIView):
    def get(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'Error': 'La empresa no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company, context={'request': request})
        return Response(serializer.data)
    

class EdificationListAV(APIView):

    def get(self, request):
        state = Edification.objects.all()
        serializer = EdificationSerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EdificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdificationDetailAV(APIView):
    def get(self, request, pk):
        try:
            edification = Edification.objects.get(pk=pk)

        except Edification.DoesNotExist:
            return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EdificationSerializer(edification)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            edification = Edification.objects.get(pk=pk)
        except Edification.DoesNotExist:
            return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EdificationSerializer(edification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            edification = Edification.objects.get(pk=pk)
        except Edification.DoesNotExist:
            return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

        edification.delete()
        return Response({'message': 'El inmueble ha sido eliminado'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def edification_list(request):
#     if request.method == 'GET':
#         state = edification.objects.all()
#         serializer = EdificationSerializer(state, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         de_serializer = EdificationSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data, status=201)
#         else:
#             return Response(de_serializer.errors, status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def edification_detail(request, id):
#     if request.method == 'GET':
#         try:
#             edification = edification.objects.get(pk=id)
#             serializer = EdificationSerializer(edification)
#             return Response(serializer.data)
#         except edification.DoesNotExist:
#             return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         edification = edification.objects.get(pk=id)
#         de_serializer = EdificationSerializer(edification, data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         try:
#             edification = edification.objects.get(pk=id)
#             edification.delete()
#         except edification.DoesNotExist:
#             return Response({'Error': 'El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)

#         return Response(status=status.HTTP_204_NO_CONTENT)
