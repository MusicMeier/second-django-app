from rest_framework import serializers
from .models import Bear, PicnicBasket

class BearSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bear
    fields = ('id', 'name', 'age')

class PicnicBasketSerializer(serializers.ModelSerializer):
  class Meta:
    model = PicnicBasket
    fields = ('id', 'sandwiches', 'bear')