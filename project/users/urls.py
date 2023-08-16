from django.urls import path
from .views import SignUpView, LoginUserView, logout_user, activate_account

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('activate_account/', activate_account, name='activate'),
]
