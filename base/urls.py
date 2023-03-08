from django.urls import path
from base import views


urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocate_list),
    path('advocates/<str:username>/', views.advocate_details)
]


