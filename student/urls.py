from django.urls import path, include
from student import views

urlpatterns = [
    # Class Based View
    path("addMentalMessages/", views.AddMentalMessages.as_view()),
    path("deleteMentalMessages/", views.DeleteMentalMessages.as_view()),
    path("updateMentalMessages/", views.UpdateMentalMessages.as_view()),
    path("getMentalMessages/", views.GetMentalMessages.as_view()),
    path("getAllMentalMessages/", views.GetAllMentalMessages.as_view()),
    path("getMentalPageList/", views.GetMentalPageList.as_view()),
]
