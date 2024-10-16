from rest_framework.response import Response
from statelist_app.models import Edification, Company, Comentary
from statelist_app.api.serializers import EdificationSerializer, CompanySerializer, ComentarySerializer
# from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from statelist_app.api.permissions import AdminOrReadOnly, ComentaryUserOrReadOnly
# Create your views here.


class ComentaryCreate(generics.CreateAPIView):
    serializer_class = ComentarySerializer

    def get_queryset(self):
        return Comentary.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        property = Edification.objects.get(pk=pk)

        user = self.request.user
        comentary_queryset = Comentary.objects.filter(
            edification=property, comentary_user=user)
        if comentary_queryset.exists():
            raise ValidationError(
                'El usuario ya escribió un comentario para esta propiedad')

        # Obtener la nueva calificación
        new_calification = serializer.validated_data['calification']

        # Calcular el nuevo promedio ponderado
        if property.number_calification == 0:
            property.avg_calification = new_calification
        else:
            total_califications = property.number_calification
            current_avg = property.avg_calification

            # Promedio ponderado
            property.avg_calification = (
                (current_avg * total_califications) + new_calification
            ) / (total_califications + 1)

        # Incrementar el número de calificaciones
        property.number_calification += 1
        property.save()

        # Guardar el comentario
        serializer.save(edification=property, comentary_user=user)


class ComentaryList(generics.ListCreateAPIView):
    # queryset = Comentary.objects.all()
    serializer_class = ComentarySerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comentary.objects.filter(edification=pk)


class ComentaryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentary.objects.all()
    serializer_class = ComentarySerializer
    permission_classes = [ComentaryUserOrReadOnly]


# class ComentaryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Comentary.objects.all()
#     serializer_class = ComentarySerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ComentaryDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comentary.objects.all()
#     serializer_class = ComentarySerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class CompanyVS(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
# class CompanyVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Company.objects.all()
#         serializers = ComentarySerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Company.objects.all()
#         edificationlist = get_object_or_404(queryset, pk=pk)
#         serializer = CompanySerializer(edificationlist)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ComentarySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         try:
#             company = Company.objects.get(pk=pk)
#         except Company.DoesNotExist:
#             return Response({'Error': 'La empresa no se encontró'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = Company(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         try:
#             company = Company.objects.get(pk=pk)
#         except Company.DoesNotExist:
#             return Response({'Error': 'La empresa no se encontró'}, status=status.HTTP_404_NOT_FOUND)

#         company.delete()
#         return Response({'message': 'La empresa ha sido eliminada'}, status=status.HTTP_204_NO_CONTENT)


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
