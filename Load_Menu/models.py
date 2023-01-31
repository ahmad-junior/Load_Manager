from django.db import models
from django.contrib import admin
from django.utils import timezone


# Navigation Items
class NavItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# Views in Admin Page
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

# Home Card Items
class CardItem(models.Model):
    title = models.CharField(max_length=50)
    pic_url = models.CharField(max_length=250)
    pic_alt = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# Home Card Items Adim Page
class CardItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'pic_url', 'pic_alt')
    
# Operators
class OperatorItem(models.Model):
    title = models.CharField(max_length=50)
    total = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

# Operators Views in Admin Page
class OperatorItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'total')

# Loads Menu
class LoadMenu(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=11)
    price = models.SmallIntegerField()
    gender = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now)
    load_type = models.CharField(max_length=20)
    operator = models.CharField(max_length=50)
    address = models.TextField(max_length=255)
    shop_keeper = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} | {self.number}"

# Load Menu in Admin List Views
class LoadMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'price', 'gender', 'date', 'load_type', 'operator', 'address', 'shop_keeper')
