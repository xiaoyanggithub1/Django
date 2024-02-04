from django.urls import path, include
from menu import views

urlpatterns = [
    # Class Based View
    path("addMenu/", views.AddMenu.as_view(), name="AddMenu"),
    path("deleteMenu/", views.DeleteMenu.as_view(), name="DeleteMenu"),
    path("updateMenu/", views.UpdateMenu.as_view(), name="UpdateMenu"),
    path("getMenu/", views.GetMenu.as_view(), name="GetMenu"),
    path("roleAddMenu/", views.RoleAddMenu.as_view(), name="RoleAddMenu"),
    path("roleDeleteMenu/", views.RoleDeleteMenu.as_view(), name="RoleDeleteMenu"),
    path("getRoleMenuIdList/", views.GetRoleMenuIdList.as_view(), name="GetRoleMenuIdList"),

]
