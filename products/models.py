from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, default=10, max_digits=8)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'This is a {self.name}'

    @property
    def checks_(self):
        return '78'


    def get_discount(self):
        # return "%.2f" %(float(self.price) * 0.95)
        return '122'
    