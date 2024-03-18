from django.urls import path,include

from .views import Logout
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [

    path('auth/',include('djoser.urls')),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('auth/logout',Logout.as_view()),
]





    