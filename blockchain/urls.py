from django.urls import path, include
from blockchain import views

urlpatterns = [
    # Class Based View
    path("getblock/", views.GetBlock.as_view(), name="AddRole"),

    path('blockchain_log/<int:pIndex>', views.BlockchainLog.as_view(), name='blockchain_log'),  # 区块日志
    path('new_block', views.NewBlock.as_view()),
    path('check', views.CheckChain.as_view()),
    path('genesis_block', views.GenesisBlock.as_view())
]
