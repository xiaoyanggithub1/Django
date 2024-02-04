from django.urls import path, include
from upload_common import views

urlpatterns = [
    # Class Based View
    path("uploadView/", views.UploadView.as_view(), name="UploadView"),
    path("deleteImageView/", views.DeleteImageView.as_view(), name="DeleteImageView"),
    path("getHomeIcon/", views.GetHomeIcon.as_view(), name="GetHomeIcon"),
    path("orderData/", views.OrderData.as_view(), name="OrderData"),
]
