from rest_framework import serializers

from products.models import Category


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']    # since i am going to delete i used oonly id(name and slug and others are not needed)