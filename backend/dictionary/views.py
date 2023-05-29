from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
# Create your views here.
from .serializers import DefinitionSerializer
from .models import Definition

# @api_view(['GET'])
# def get_definitions(request):
#     # category_id = request.GET.get('category_id', '')
#     definitions = Definition.objects.all()

#     # if category_id:
#     #     courses = courses.filter(categories__in=[int(category_id)])

#     serializer = DefinitionSerializer(definitions, many=True)
#     return Response(serializer.data)



# class AuthorDetailView(RetrieveAPIView):
#     permission_classes = (AllowAny, )
#     serializer_class = AuthorSerializer
#     queryset = Author.objects.all()


class DefinitionListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DefinitionSerializer
    queryset = Definition.objects.all()


class DefinitionCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DefinitionSerializer
    queryset = Definition.objects.all()

class DefinitionDetailView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DefinitionSerializer
    queryset = Definition.objects.all()
    lookup_field = 'slug'

class DefinitionUpdateView(UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DefinitionSerializer
    queryset = Definition.objects.all()

class DefinitionDeleteView(DestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Definition.objects.all()