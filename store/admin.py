from django.contrib import admin
from store.models import Category, Product, ProductChoose, ProductShow, ProductOff, Customer, Order, Profile
from django.contrib.auth.models import User



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductShow)
admin.site.register(ProductChoose)
admin.site.register(ProductOff)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Profile)


class ProfileInLine(admin.StackedInline):
    model = Profile



class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInLine]


admin.site.unregister(User)


admin.site.register(User, UserAdmin)
