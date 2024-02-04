from django.urls import path, include
from middleware import views

urlpatterns = [
    # Class Based View
    path("login/", views.LoginView.as_view(), name="login"),
]
