from django.urls import include, path
from store import views
#from .serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserPasswordResetSerializer
from .views import *
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path
#from .views import ProductListCreateView, ProductDetailView, OrderCreateView,OrderDetailView, OrderListView, OrderItemCreateView,OrderItemDetailView,UserProfileView,UserLoginView,UserRegistrationView
   
  
urlpatterns = [
    path('store/register/', UserRegistrationView.as_view(), name='register'),
    path('store/login/', UserLoginView.as_view(), name='login'),
    path('store/profile/', UserProfileView.as_view(), name='profile'),
    path('store/profile/update/', UserProfileUpdateAPIView.as_view(), name='profile-update'),
    path('store/changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('store/send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('store/reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('store/products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('store/products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('store/orders/', OrderCreateView.as_view(), name='order_create'),
    path('store/orders/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('store/order-items/', OrderItemCreateView.as_view(), name='order_item_create'),
    path('store/order-items/<int:pk>/', OrderItemDetailView.as_view(), name='order_item_detail'),
    path('store/user-orders/', OrderListView.as_view(), name='order_list'),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




