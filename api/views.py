from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import ProgammerSerializer,PersonSerializer
from .models import Programmer, Person
import datetime
from django_filters.rest_framework import DjangoFilterBackend
from api.utils.filter import PersonFilter
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.
#ORM OBJECT REALTIONAL MAPPING
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset=Programmer.objects.all()
    serializer_class=ProgammerSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.filter(
        deleted_at__isnull=True
    )
    serializer_class = PersonSerializer

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = [            
        "names",
        "last_names",
        "document_type"
    ]
    filterset_class = PersonFilter
    ordering_fields = ["created_at"]

    def destroy(self, request, *args, **kwargs ):
        instance = self.get_object()
        instance.deleted_at = datetime.datetime.now()
        count_documents = (
            Person.objects.filter(
                document__icontains = instance.document + '_deleted'
            ).values('document').count()
        )
        print("count_documents ", count_documents)
        instance.document = instance.document + '_deleted' + str(count_documents + 1)
        instance.save()
        return Response(
            {"message": "Eliminado Exitosamente"},
            status=status.HTTP_200_OK
        )
    
    