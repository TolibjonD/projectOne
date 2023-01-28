from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class AllProducts(models.Model):
    nomi = models.CharField(max_length=250)
    miqdori = models.PositiveIntegerField()
    miqdor_birligi = models.CharField(max_length=150, help_text="O'lchov birligini kiriting: Kg, Tonna, Vagon, Litr, Dona", null=True)
    birlik_narxi = models.FloatField(null=True)
    tavsif = models.TextField()
    photo = models.ImageField(upload_to='images/' , default="images/no-image.jpg")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def get_absolute_url(self):
        return reverse("info", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.nomi    

class SoldProducts(models.Model):
    product = models.ForeignKey(AllProducts,on_delete=models.CASCADE, related_name="soldproducts")
    miqdori = models.PositiveIntegerField(
        null=True, help_text="Sotilgan mahsulot miqdorini kiriting."
    )
    sold_product_price = models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    def get_absolute_url(self):
        return reverse("products/list")
    

    def __str__(self):
        return self.product.nomi   