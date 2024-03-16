from django_filters import rest_framework
from api.models import Person

class PersonFilter(rest_framework.FilterSet):
    class Meta:
        model = Person
        fields = (
            "names",
            "last_names",
            "document_type"
        )