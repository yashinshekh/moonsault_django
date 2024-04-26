from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('update_text/<int:pk>/', views.update_text, name='update_text'),
    path('update_image/<int:pk>/', views.update_image, name='update_image'),
]
