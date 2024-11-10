from django.contrib import admin
from django.urls import path, include
from calculator import views  # 追加: viewsモジュールのインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculate, name='home'),  # ルートURLを設定
    path('calculate/', views.calculate, name='calculate'),
    path('accounts/', include('django.contrib.auth.urls')),  # ログイン関連のパス
]
