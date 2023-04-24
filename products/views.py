from rest_framework import generics, mixins
from .serializers import ProductSerializer, BannerSerializer
from .models import Product, Banner
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404


class ProductView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


class BannerView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


def product_detail(request: HttpRequest, slug):
    product = get_object_or_404(Product, slug=slug)
    image_urls = [request.build_absolute_uri(image.image.url) for image in product.images.all()]
    response_data = {
        'name': product.name,
        'images': image_urls,
        'price': product.price,
        'details': product.details,
        'slug': product.slug,
    }
    return JsonResponse(response_data)


def index(request):
    return HttpResponse("Welcome To Mikes`s API, Nothing to see here Goodbye :)")
