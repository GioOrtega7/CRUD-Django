from rest_framework import serializers
from .models import Programmer, Person

class ProgammerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Programmer
        #fields=('fullname','nickname')
        fields='__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        #fields='__all__'
        exclude=["deleted_at"]