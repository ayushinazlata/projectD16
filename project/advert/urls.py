from django.urls import path
from .views import AdvertsList, AdvertDetail, AdvertCreate, AdvertEdit, AdvertDelete, ReactionCreate, ReactionsList, \
    UserAdvertsList

urlpatterns = [
    path('', AdvertsList.as_view(), name='adverts_list'),
    path('<int:pk>/', AdvertDetail.as_view(), name='advert_detail'),
    path('my/', UserAdvertsList.as_view(), name='user_adverts'),
    path('create/', AdvertCreate.as_view(), name='advert_create'),
    path('<int:pk>/edit/', AdvertEdit.as_view(), name='advert_edit'),
    path('<int:pk>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    path('<int:pk>/reaction/create', ReactionCreate.as_view(), name='reaction_create'),
    path('reactions/', ReactionsList.as_view(), name='reactions_list'),
]
