from django.urls import path
from .views import (AdvertsListView, AdvertDetailView, UserAdvertsListView, AdvertCreateView, AdvertUpdateView,
                    AdvertDeleteView, ReactionCreateView, ReactionsListView, approved, ReactionsDeleteView, )

urlpatterns = [
    path('', AdvertsListView.as_view(), name='adverts_list'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='advert_detail'),
    path('my_adverts/', UserAdvertsListView.as_view(), name='user_adverts'),
    path('create/', AdvertCreateView.as_view(), name='advert_create'),
    path('<int:pk>/update/', AdvertUpdateView.as_view(), name='advert_update'),
    path('<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert_delete'),
    path('<int:advert_id>/reaction/create/', ReactionCreateView.as_view(), name='reaction_create'),
    path('reactions/', ReactionsListView.as_view(), name='reactions_list'),
    path('reactions/<int:reaction_id>/approved/', approved, name='approved'),
    path('reactions/<int:pk>/delete/', ReactionsDeleteView.as_view(), name='reaction_delete'),
]
