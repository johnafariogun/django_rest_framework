from django.urls import path
from products import views
from .views import ProductDetailAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView, ProductMixinView


urlpatterns = [
    path("<int:pk>/", ProductDetailAPIView.as_view()),
    path("<int:pk>/delete/", ProductDeleteAPIView.as_view()),
    path("<int:pk>/update/", ProductUpdateAPIView.as_view()),
    path("", ProductListCreateAPIView.as_view()),
    # path("", ProductMixinView.as_view()),
    # path('<int:pk>/', ProductMixinView.as_view()),
    

]