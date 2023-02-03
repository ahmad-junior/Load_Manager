from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NavItem, CardItem, OperatorItem, LoadMenu
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def home(request):
    NavItems = NavItem.objects.all()
    cards = CardItem.objects.all()
    operators = OperatorItem.objects.all()
    recents = LoadMenu.objects.all()[:10]
    
    # Make total price of all Load on home page
    # Make all operators total price 0
    for op in operators:
        op.total = 0
    # Add all price to total price
    for op in operators:
        # Filter all today load
        todayLoad = LoadMenu.objects.all().filter(operator = op.title, date = timezone.now().date())
        op.list = todayLoad.values_list('price', flat=True) # Get all price of today load
        for x in op.list:
            op.total += x


    params = {"NavItems": NavItems, "cards": cards, "operators": operators, "recents": recents}
    return render(request, "home.html", params)

# Add Page
def add(request):
    NavItems = NavItem.objects.all()
    cards = CardItem.objects.all()
    operators = OperatorItem.objects.all()
    try:
        max_value = int(LoadMenu.objects.values().last()['id']) + 1
    except Exception as e:
        max_value = 1
    # Date fomat yyyy-mm-dd
    today = timezone.now().date().strftime("%Y-%m-%d")
    params = {"NavItems": NavItems, "cards": cards, "operators": operators, "max_value": max_value, "today": today}
    return render(request, "add.html", params)

# Add item to dataBase
def handleAddItem(request):
    if request.method == "POST":
        id = request.POST['add_id']
        name = request.POST['add_name']
        number = request.POST['add_number']
        price = request.POST['add_price']
        gender = request.POST['add_gender']
        date = request.POST['add_date']
        load_type = request.POST['add_load_type']
        operator = request.POST['add_operator']
        address = request.POST['add_address']
        shop_keeper = request.POST['add_shop_keeper']
        
        isNumber = False
        
        try:
            if int(number) > 0:
                isNumber = True
            else:
                isNumber = False
        except:
            message_allert = f"You have enter invalid Phone Number Please Enter a valid."
            messages.error(request, message_allert)
            return redirect('HomePage')
        
        # Form Validation
        if isNumber:
            newLoatItem = LoadMenu(id=id, name=name, number=number, price=price, gender=gender, date=date, load_type=load_type, operator=operator, address=address, shop_keeper=shop_keeper)
            newLoatItem.save()
            
            # Allert Message and redirect to the Home
            message_allert = f"You have successfully added a new item {newLoatItem.name} | {newLoatItem.number} to the database"
            messages.success(request, message_allert)
        
            return redirect('HomePage')
        else:
            message_allert = f"Error your record can't able to add in our database! Try to add a valid record."
            messages.error(request, message_allert)
            return redirect('HomePage')
    else:
        return HttpResponse(request, "Error")

# View All database
def view(request):
    NavItems = NavItem.objects.all()
    loadMenus = LoadMenu.objects.all()
    params = {"NavItems": NavItems, "loadMenus": loadMenus}
    return render(request, "view.html", params)

# Delete item Page
def delete(request):
    NavItems = NavItem.objects.all()
    params = {"NavItems": NavItems}
    return render(request, "delete.html", params)

def update(request):
    NavItems = NavItem.objects.all()
    params = {"NavItems": NavItems}
    return render(request, "update.html", params)

# Preview item Page
def previewDelete(request):
    if request.method == "POST":
        NavItems = NavItem.objects.all()
        searchItem = request.POST['inputItem']
        try:
            int(searchItem)
            if len(searchItem) > 11 or len(searchItem) < 11:
                searchItem = f"{searchItem} is not a phone number"
        except:
            searchItem = f"{searchItem} is not a phone number"
        items = LoadMenu.objects.all().filter(number = searchItem).values()
        params = {"NavItems": NavItems, "items": items, "searchItem": searchItem}
        return render(request, "previewItemsDelete.html", params)
    else:
        return HttpResponse(request, "Error")
    
def previewUpdate(request):
    if request.method == "POST":
        NavItems = NavItem.objects.all()
        searchItem = request.POST['inputItem']
        try:
            int(searchItem)
            if len(searchItem) > 11 or len(searchItem) < 11:
                searchItem = f"{searchItem} is not a phone number"
        except:
            searchItem = f"{searchItem} is not a phone number"
        
        items = LoadMenu.objects.all().filter(number = searchItem).values()
        params = {"NavItems": NavItems, "items": items, "searchItem": searchItem}
        return render(request, "previewItemsUpdate.html", params)
    else:
        return HttpResponse(request, "Error")

def handleUpdateItem(request):
    if request.method == "POST":
        id = request.POST['add_id']
        name = request.POST['add_name']
        date = request.POST['add_date']
        number = request.POST['add_number']
        price = request.POST['add_price']
        gender = request.POST['add_gender']
        load_type = request.POST['add_load_type']
        operator = request.POST['add_operator']
        address = request.POST['add_address']
        shop_keeper = request.POST['add_shop_keeper']
        
        itemToUpdate = LoadMenu.objects.all().get(id=id)

        itemToUpdate.id = id        
        itemToUpdate.date = date 
        itemToUpdate.name = name
        itemToUpdate.number = number
        itemToUpdate.price = price
        itemToUpdate.gender = gender
        itemToUpdate.load_type = load_type
        itemToUpdate.operator = operator
        itemToUpdate.address = address
        itemToUpdate.shop_keeper = shop_keeper
        
        itemToUpdate.save()
        
        mes_alt = f"Updated Successfully!"
        messages.success(request, mes_alt)
        return redirect('HomePage')
    else:
        mes_alr = f"Unknown Error! Please try again!"
        messages.success(request, mes_alt)
        return redirect('HomePage')

def itemPriewToUpdate(request):
    if request.method == "POST":
        IdToHandle = request.POST['IdToHandle']
        today = timezone.now().date().strftime("%Y-%m-%d")
        loadItem = LoadMenu.objects.all().get(id = IdToHandle)
        NavItems = NavItem.objects.all()
        params = {"NavItems": NavItems, "loadItem": loadItem, "today":today}
        return render(request, "loadItemUpdate.html", params)
    else:
        return HttpResponse(request, "Error")

# Actions
def itemPriewToDelete(request):
    if request.method == "POST":
        IdToHandle = request.POST['IdToHandle']
        loadItem = LoadMenu.objects.all().get(id = IdToHandle)
        NavItems = NavItem.objects.all()
        params = {"NavItems": NavItems, "loadItem": loadItem}
        return render(request, "loadItemDelete.html", params)
    else:
        return HttpResponse(request, "Error")

def handleDeleteItem(request):
    if request.method == "POST":
        id = request.POST['add_id']
        itemToDelete = LoadMenu.objects.all().get(id=id)
        mes_alr = f"You have successfully Removed {itemToDelete.name} | {itemToDelete.number} from database."
        itemToDelete.delete()
        messages.success(request, mes_alr)
        return redirect('HomePage')
    else:
        mes_alr = f"Unknown Error! Please try again!"
        messages.error(request, mes_alr)
        return redirect('HomePage')
