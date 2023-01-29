from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import AllProducts, SoldProducts
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class FinishedProductsView(LoginRequiredMixin, View):
    def get(self, request):
        products = AllProducts.objects.all().filter(miqdori=0)
        paginator = Paginator(products, 4)
        current_page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(current_page_number)
        return render(
            request,
            "finished.html",
            {"page_obj":page_obj}
        )


class SoldPrListView(LoginRequiredMixin ,ListView):
    def get(self, request):
        products = SoldProducts.objects.all().order_by('-id')
        paginator = Paginator(products, 4)
        current_page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(current_page_number)
        return render(
            request,
            "sold_list.html",
            {"page_obj":page_obj}
        )
        
class SoldProductsView(LoginRequiredMixin ,CreateView):
    def get(self, request):
        pr_id = request.GET.get('product')
        product = AllProducts.objects.get(id=pr_id)
        return render(request, "sold.html", {"product":product})

    def post(self, request):
        sold_product = request.POST['sold_product']
        product_id = request.POST['product_id']
        sold_product_price = request.POST['sold_product_price']
        if product_id and sold_product:
            product = AllProducts.objects.get(id=product_id)
            SoldProducts.objects.create(
                product = AllProducts.objects.get(id=product_id),
                miqdori = sold_product,
                sold_product_price = sold_product_price
            )
            product.miqdori = int(product.miqdori) - int(sold_product)
            product.save()
            messages.success(request,"Mahsulot muvaffaqiyatli sotilganlarga joylandi .")
            return redirect("products")

class ProductCreateVeiw(LoginRequiredMixin , SuccessMessageMixin ,CreateView):
    model = AllProducts
    template_name = "add.html"
    fields = ("nomi" , "miqdori", "miqdor_birligi" , "birlik_narxi", "sotiladigan_narxi" , "tavsif" , "photo")
    success_message = "Maxsulot muvaffaqiyatli ravishda qo'shildi ."

class PrDetailView(LoginRequiredMixin , DetailView):
    model = AllProducts
    template_name = "info.html"
        

# class PrListView(LoginRequiredMixin ,ListView):
#     model = AllProducts
#     template_name = "list.html"
class PrListView(LoginRequiredMixin, View):
    def get(self, request):
        products = AllProducts.objects.all().order_by('-id')
        search_query = request.GET.get('q' , '')
        if search_query:
            products = AllProducts.objects.all().filter(nomi__icontains=search_query)
        paginator = Paginator(products, 4)
        current_page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(current_page_number)
        return render(
            request,
            "list.html",
            {"page_obj":page_obj, "search":search_query}
        )

class PrUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = AllProducts
    template_name = "update.html"
    fields = ("nomi" , "miqdori", "miqdor_birligi" , "birlik_narxi" , "sotiladigan_narxi" , "tavsif" , "photo")
    success_message = "Ma'lumotlar muvaffaqiyatli ravishda yangilandi ."

class PrDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = AllProducts
    success_url = reverse_lazy("products")
    template_name = 'delete.html'
    success_message = "Maxsulot muvaffaqiyatli ravishda o'chirildi ."