from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    details = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    buttonText = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    smallText = models.CharField(max_length=100)
    midText = models.CharField(max_length=100)
    largeText = models.CharField(max_length=100)
    largeText2 = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    saleTime = models.CharField(max_length=100)

    def __str__(self):
        return self.product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
