from django.urls import path, include
from role import views

urlpatterns = [
    # Class Based View
    path("addRole/", views.AddRole.as_view(), name="AddRole"),
    path("deleteRole/", views.DeleteRole.as_view(), name="DeleteRole"),
    path("updateRole/", views.UpdateRole.as_view(), name="UpdateRole"),
    path("getRole/", views.GetRole.as_view(), name="GetRole"),
    path("getAllRoles/", views.GetAllRoles.as_view(), name="GetAllRoles"),
    # path("addRole/", views.AddRole.as_view(), name="AddRole"),
]
