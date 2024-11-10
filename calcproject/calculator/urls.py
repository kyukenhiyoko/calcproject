from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate, name='calculate'),  # 計算ページ
    # 他のURLパターン
]
