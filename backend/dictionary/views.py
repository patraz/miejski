from rest_framework.permissions import AllowAny
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