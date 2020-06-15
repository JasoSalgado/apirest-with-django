from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    """
    To not replicate lots of information, we use ModelSerializer
    """
    class Meta:
        model = Country
        fields = '__all__'
