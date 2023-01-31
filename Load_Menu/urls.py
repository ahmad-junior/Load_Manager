
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "HomePage"),
    path('add', views.add, name = "AddPage"),
    path('resultAdd', views.handleAddItem, name = "HandleAddItem"),
    path('views' , views.view, name = "ViewPage"),
    path('delete' , views.delete, name = "DeletePage"),
    path('update' , views.update, name = "DeletePage"),
    path('previewItemsDelete' , views.previewDelete, name = "previewItemsDelete"),
    path('itemPreviewDelete', views.itemPriewToDelete, name = "ItemPreviewPageDelete"),
    path('previewItemsUpdate' , views.previewUpdate, name = "previewItemsUpdate"),
    path('itemPreviewUpdate', views.itemPriewToUpdate, name = "ItemPreviewPageUpdate"),
    path('deleteItem', views.handleDeleteItem, name = "DeleteItem"),
    path('updateItem', views.handleUpdateItem, name = "UpdateItem"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
