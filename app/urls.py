from django.urls import path
from app import views
from .views import ProfileView, ContactView, CompleteView

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('complete/', views.CompleteView.as_view(), name='complete'),
]