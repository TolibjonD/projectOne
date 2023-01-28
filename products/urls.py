from django.urls import path
from .views import HomePageView, ProductCreateVeiw, PrDetailView, PrListView, PrUpdateView, PrDeleteView, SoldProductsView, SoldPrListView, FinishedProductsView

urlpatterns = [
    path('products/sold/' ,SoldPrListView.as_view() , name="sold_list"  ),
    path('notAvailable/' , FinishedProductsView.as_view() , name="noproducts"),
    path('sold/' , SoldProductsView.as_view() , name="sold" ),
    path('add/' , ProductCreateVeiw.as_view() , name="add"),
    path('products/<int:pk>/update/' , PrUpdateView.as_view() , name="update"),
    path("products/<int:pk>/" , PrDetailView.as_view() , name="info"),
    path('products/' , PrListView.as_view() , name="products"),
    path("products/<int:pk>/delete/" , PrDeleteView.as_view() , name="delete" ),
    path('' , HomePageView.as_view() , name='home'),
]
