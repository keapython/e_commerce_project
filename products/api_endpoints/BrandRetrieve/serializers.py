from rest_framework import serializers

from products.models import Brand

class BrandRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'slug',
            'logo'
        ]