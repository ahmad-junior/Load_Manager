from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NavItem, OperatorItem, LoadMenu, OperatorItem
from django.contrib import messages
from django.utils import timezone
from .backValidations import isValid
from django.db.models import Q

# Create your views here.
# Login Page
def login(request):
    if request.method == "POST":
        # User Credientials
        userName = request.POST['userNameLogin']
        userPassword = request.POST['userPasswordLogin']
        
        # Puzzle
        OPOne = request.POST['OPOne']
        OPTwo = request.POST['OPTwo']
        isNotRebootSollution = request.POST['isNotRebootSollution']
        
        
        try:
            if int(OPOne) + int(OPTwo) == int(isNotRebootSollution):
                return HttpResponse("good")
            else:
                return HttpResponse("bad")
        except: 
            pass
    else:
        return render(request, "login_page.html")
        
        # params = {"User Name": userName}
        
        # return HttpResponse(params.items())

# SinUp Page
def sinup(request):
    if request.method == "POST":
        # User Credientials
        userName = request.POST['userNameSinup']
        userPassword = request.POST['userPasswordSinup']
        userPasswordConfirm = request.POST['userPasswordSinupConfirm']
        
        # Puzzle
        OPOne = request.POST['OPOne']
        OPTwo = request.POST['OPTwo']
        isNotRebootSollution = request.POST['isNotRebootSollution']
        
        try:
            if int(OPOne) + int(OPTwo) == int(isNotRebootSollution):
                return HttpResponse("good")
            else:
                return HttpResponse("bad")
        except: 
            pass
    else:
        return render(request, "sinup_page.html")


# Home Page
def home(request):
    NavItems = NavItem.objects.all()
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


    params = {"NavItems": NavItems, "operators": operators, "recents": recents}
    return render(request, "home.html", params)

# Add Item
def add(request):
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
        
        addToDatabase = isValid(request, id, name, number, price, gender, load_type, operator, address, shop_keeper)
        
        if addToDatabase:
            newLoadItem = LoadMenu(id=id, name=name, number=number, price=price, gender=gender, date=date, load_type=load_type, operator=operator, address=address, shop_keeper=shop_keeper)
            newLoadItem.save()
            messages.success(request, "Load added successfully!")
        else:
            pass

        return redirect('HomePage')
    else:
        NavItems = NavItem.objects.all()
        operators = OperatorItem.objects.all()
        try:
            max_value = int(LoadMenu.objects.values().last()['id']) + 1
        except Exception as e:
            max_value = 1
        # Date fomat yyyy-mm-dd
        today = timezone.now().date().strftime("%Y-%m-%d")
        params = {"NavItems": NavItems, "operators": operators, "max_value": max_value, "today": today}
        return render(request, "add.html", params)

# View All database
def view(request):
    NavItems = NavItem.objects.all()
    loadMenus = LoadMenu.objects.all()
    params = {"NavItems": NavItems, "loadMenus": loadMenus}
    return render(request, "view.html", params)

# Delete Item
def delete(request):
    if request.method == "POST":
        id = request.POST['add_id']
        itemToDelete = LoadMenu.objects.all().get(id=id)
        
        if not LoadMenu.objects.all().filter(id=id).exists:
            messages.error(request, "Something went wrong!")
        else:
            itemToDelete.delete()
            mes_alr = f"You have successfully Removed {itemToDelete.name} | {itemToDelete.number} from database."
            messages.success(request, mes_alr)
        
        return redirect('HomePage')
    else:
        NavItems = NavItem.objects.all()
        params = {"NavItems": NavItems}
        return render(request, "delete.html", params)

# Update Item
def update(request):
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
        
        updateToDatabase = isValid(request, id, name, number, price, gender, load_type, operator, address, shop_keeper, addItem=False)
        
        if updateToDatabase:
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
            messages.success(request, "Load added successfully!")
        else:
            pass
        return redirect('HomePage')
    else:
        NavItems = NavItem.objects.all()
        params = {"NavItems": NavItems}
        return render(request, "update.html", params)

# Preview item Page To Delete
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
    
# Preview item Page To Update
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

# Load Item Preview for Update
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

# Load Item Preview for Delete
def itemPriewToDelete(request):
    if request.method == "POST":
        IdToHandle = request.POST['IdToHandle']
        loadItem = LoadMenu.objects.all().get(id = IdToHandle)
        NavItems = NavItem.objects.all()
        params = {"NavItems": NavItems, "loadItem": loadItem}
        return render(request, "loadItemDelete.html", params)
    else:
        return HttpResponse(request, "Error")


# Search Engine
def searchEngine(request):
    if request.method == "POST":
        searchItem = request.POST['inputItem']
        
        itemsFound = LoadMenu.objects.filter(Q(id__icontains=searchItem) | Q(name__icontains=searchItem) | Q(number__icontains=searchItem) | Q(address__icontains=searchItem))
        NavItems = NavItem.objects.all()
        return render(request, "search.html", {"itemsFound": itemsFound, "NavItems": NavItems, "searchItem": searchItem})