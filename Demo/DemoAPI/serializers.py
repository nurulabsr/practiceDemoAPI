from rest_framework import serializers
from .models import DemoModel
# from .models import Category


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoModel
        # field = ['id', 'price', 'description']
        fields = '__all__'
        