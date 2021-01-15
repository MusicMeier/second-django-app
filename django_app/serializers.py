from rest_framework import serializers
from .models import Bear

class BearSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bear
    fields = ('id', 'name', 'age')