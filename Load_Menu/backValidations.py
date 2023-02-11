from django.shortcuts import redirect
from django.contrib import messages
from .models import LoadMenu, OperatorItem

def isValid(request, id, name, number, price, gender, load_type, operator, address, shop_keeper, addItem=True):
    genders = ['Male', 'Female', 'Other']
    load_types = ['E - Load', 'Package', 'Other']
    operators = OperatorItem.objects.all().values_list('title', flat=True)
    addIt, updateIt = False, False
        
    # Form Validation in backend
    if addItem:
        if id == "" or LoadMenu.objects.all().filter(id = id).exists():
            messages.error(request, "Please provide a valid id! To add Item")
            addIt =  False
        else:
            addIt = True
    else:
        if not LoadMenu.objects.all().filter(id = id).exists():
            messages.error(request, "Please provide a valid id! To update item")
            updateIt =  False
        else:
            updateIt =  True

    if not (addIt or updateIt):
        messages.error(request, "Error In ID!")
        return False
    elif len(name) < 2 or len(name) > 50:
        messages.error(request, "Name must be between 2 to 50 characters")
        return False
    elif len(number) < 11 or len(number) > 11 or not number.isdigit():
        messages.error(request, "Number must be 11 characters and must be digit")
        return False
    elif int(price) < 80:
        messages.error(request, "Price must be greater than 80")
        return False
    elif gender not in genders:
        messages.error(request, "Please provide a valid gender!")
        return False
    elif load_type not in load_types:
        messages.error(request, "Please provide a valid load type!")
        return False
    elif operator not in operators:
        messages.error(request, "Please provide a valid operator!")
        return False
    elif len(address) < 5 or len(address) > 100:
        messages.error(request, "Please provide a valid address! Address must be between 5 to 100 characters")
        return False
    elif len(shop_keeper) < 2:
        messages.error(request, "Please provide a valid shop keeper name!")
        return False
    else:
        return True