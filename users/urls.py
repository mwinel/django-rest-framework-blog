from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UsersAPIView, CustomTokenObtainPairView

urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('auth/jwt/', CustomTokenObtainPairView.as_view()),
    path('auth/jwt/refresh/', TokenRefreshView.as_view())
]
