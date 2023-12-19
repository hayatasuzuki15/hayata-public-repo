from django.contrib import admin
from django.urls import path, include
from .views import Menu,BlogList,BlogDetail,BlogCreate

urlpatterns = [
    path("", Menu.as_view(),name="menu"),
    path("list/", BlogList.as_view(),name="list_mod"),
    path("detail/<int:pk>/", BlogDetail.as_view(),name="detail_mod"),
    path("create/",BlogCreate.as_view(),name="create_mod"),
]
