from rest_framework import serializers
from .models import Product, Banner, ProductImage



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'images', 'price', 'details', 'slug']

    def get_images(self, obj):
        images = obj.images.all()
        return [self.context['request'].build_absolute_uri(image.image.url) for image in images]


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['buttonText', 'product', 'desc', 'smallText', 'midText', 'largeText', 'largeText2', 'discount',
                  'saleTime', 'image']
