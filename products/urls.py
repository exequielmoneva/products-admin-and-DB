from django.urls import path

from .views import ProductViewSet, UserApiView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'get_all_products',
        'post': 'create_product',
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'get_single_product',
        'put': 'update_product',
        'delete': 'delete_product',
    })),
    path('user', UserApiView.as_view()),
]
