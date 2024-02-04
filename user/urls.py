from django.urls import path, include
from user import views

urlpatterns = [
    # Class Based View
    path("addUser/", views.AddUser.as_view(), name="addUser"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="Logout"),
    path("currentUser/", views.CurrentUser.as_view(), name="CurrentUser"),
    path("deleteUser/", views.DeleteUser.as_view(), name="DeleteUser"),
    path("updateUser/", views.UpdateUser.as_view(), name="UpdateUser"),
    path("getUserById/", views.GetUserById.as_view(), name="GetUserById"),
    path("getAllUsers/", views.GetAllUsers.as_view(), name="GetAllUsers"),
    path("getUserPageList/", views.GetUserPageList.as_view(), name="GetUserPageList"),
    path("userAddRole/", views.UserAddRole.as_view(), name="UserAddRole"),
    path("userDeleteRole/", views.UserDeleteRole.as_view(), name="UserDeleteRole"),
    path("userRoleIdList/", views.UserRoleIdList.as_view(), name="UserRoleIdList"),
    path("userRoute/", views.UserRoute.as_view(), name="UserRoute"),
]
