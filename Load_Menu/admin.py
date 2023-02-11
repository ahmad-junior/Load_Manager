from django.contrib import admin
from .models import NavItem, NavItemAdmin, OperatorItem, OperatorItemAdmin,LoadMenu, LoadMenuAdmin
# Register your models here.
admin.site.register(NavItem, NavItemAdmin)
admin.site.register(OperatorItem, OperatorItemAdmin)
admin.site.register(LoadMenu, LoadMenuAdmin)