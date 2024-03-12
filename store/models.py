from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save 


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(user, auto_now=True)
    phone = models.CharField(max_length=11, blank=True, verbose_name='تلفن')
    app =  models.CharField(max_length=3, blank=True, verbose_name='پیام رسان')
    city =  models.CharField(max_length=50, blank=True, verbose_name='شهر')
    address1 = models.CharField(max_length=300, blank=True, verbose_name='ادرس')
    post = models.CharField(max_length=10, blank=True, verbose_name='کدپستی')
    old_cart = models.CharField(max_length=300, blank=True, null=True, verbose_name='سبد خرید')

    def __str__(self):
        return self.user.username


#create profile when user sign up 
def create_profile(sender, instance, created, **kwargs):

    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)




class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/category/')
    description_up =  models.CharField(max_length=250, default='', blank=True, null=True)
    description = models.CharField(max_length=550, default='', blank=True, null=True)
    description_sub =  models.CharField(max_length=250, default='', blank=True, null=True)
    shop_page = models.BooleanField(default=False)
    show_page = models.BooleanField(default=False)
    amade_page = models.BooleanField(default=False)
    nemone_page = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'دسته بندی'



class ProductShow(models.Model):
    name = models.CharField(max_length=150)
    description_up =  models.CharField(max_length=250, default='', blank=True, null=True)
    description = models.CharField(max_length=550, default='', blank=True, null=True)
    description_sub =  models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'محصول ساختنی'

# must add discrption for product
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    discrption = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    status= models.BooleanField(default=True)
    is_posti = models.BooleanField(default=False, verbose_name='پستی')
    is_tape = models.BooleanField(default=False, verbose_name='چسب')
    is_ready = models.BooleanField(default=False, verbose_name='جعبه اماده')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'محصول آماده'



class ProductOff(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    discrption = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    status= models.BooleanField(default=True)
    is_posti = models.BooleanField(default=False, verbose_name='پستی')
    is_tape = models.BooleanField(default=False, verbose_name='چسب')
    is_ready = models.BooleanField(default=False, verbose_name='جعبه اماده')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'محصول تخفیفی'
        

class ProductChoose(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/product_di/')
    daroyi = models.BooleanField(default=False, verbose_name='دارویی')
    mamoli = models.BooleanField(default=False, verbose_name='معمولی')
    pitzayi = models.BooleanField(default=False, verbose_name='پیتزایی')
    sini = models.BooleanField(default=False, verbose_name='سینی')
    snack = models.BooleanField(default=False, verbose_name='اسنک')
    tahghofli = models.BooleanField(default=False, verbose_name='ته قفلی')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'نمونه دایکاتی ها'


class Customer(models.Model):
    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    address =models.CharField(max_length=400, blank=True, null=True)
    postal_code =models.CharField(max_length=10)
    city = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name_plural = 'مشتری'
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,  related_name='r_customer')
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=400, default='', blank=False, null=False)
    phone = models.CharField(max_length=11, )
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False, verbose_name='وضعیت ارسال')

    def __str__(self):
        return f' سفارش {self.product} برای {self.customer.first_name}'
    
    class Meta:
        verbose_name_plural = 'سفارشات'
    

