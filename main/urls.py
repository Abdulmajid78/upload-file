from django.urls import path
from .views import HomeView, ContactCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/create/', ContactCreateView.as_view(), name='contact_create')
]
