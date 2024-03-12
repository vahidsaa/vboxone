from django.db import models

from django.contrib.auth.models import User



class ShippingAdress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=555)
    codeposti = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=55, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'ادرس های تحویل'


    def __str__(self):
        return f'address - {str(self.id)} - {str(self.user.username)}'