from rest_framework import serializers
from models import New, CategoryNews


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('title',)


class CategoryNewsSerializer(serializers.ModelSerializer):
    new_cateogory = NewSerializer(many=True)


    class Meta:
        model = CategoryNews
        fields = ('category_name', 'new_cateogory')
