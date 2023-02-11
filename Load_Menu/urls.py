from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "HomePage"),
    path('login', views.login, name = "LoginPage"),
    path('sinup', views.sinup, name = "SinupPage"),
    path('add', views.add, name = "AddPage"),
    path('views' , views.view, name = "ViewPage"),
    path('delete' , views.delete, name = "DeletePage"),
    path('update' , views.update, name = "DeletePage"),
    path('previewItemsDelete' , views.previewDelete, name = "previewItemsDelete"),
    path('itemPreviewDelete', views.itemPriewToDelete, name = "ItemPreviewPageDelete"),
    path('previewItemsUpdate' , views.previewUpdate, name = "previewItemsUpdate"),
    path('itemPreviewUpdate', views.itemPriewToUpdate, name = "ItemPreviewPageUpdate"),
    path('searchEngine', views.searchEngine, name = "SearchEnginePage"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
