from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    searchView,
    StringsView,
    WindsView,
    BrassView,
    AccessoryView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('strings/', StringsView.as_view(), name='strings'),
    path('accessories/', AccessoryView.as_view(), name='accessory'),
    path('brass/', BrassView.as_view(), name='brass'),
    path('woodwinds/', WindsView.as_view(), name='winds'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('search/', searchView.as_view(), name='search'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
