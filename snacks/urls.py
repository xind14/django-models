from django.urls import path
from .views import SnackListView, SnackDetailView, AboutPageView

urlpatterns = [
  path('', SnackListView.as_view(), name='snack_list'),
  path('about/', AboutPageView.as_view(), name='about'),
  path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
]