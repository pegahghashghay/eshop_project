# from django.db.models import Q
#
# from django.shortcuts import render, get_object_or_404
# from .models import Product, ProductCategory
# from django.http import Http404
# from django.db.models import Avg, Min, Max
#
#
# # Create your views here.
#
# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     return render(request, 'product_module/product_list.html', {
#         'products': products,
#     })
#
#
# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product_module/product_detail.html', {
#         'product': product
#     })
#
#
# def product_item_partial(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'includes/product_item_partial.html', {
#         'product': product
#     })
#
import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand, ProductVisit
from django.db.models import Count
from site_module.models import SiteBanner
from utils.http_service import get_client_ip
from product_module.mongo import product_favorite
from product_module.mongo import product_detail
from product_module.mongo import product_list





class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 2

    # def get_queryset(self):
    #     base_query = super(ProductListView, self).get_queryset()
    #     data = base_query.filter(is_active=True)
    #     return data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()  # کل محصولات میخواد
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPositions.product_list)
        product_list(product.title, product.price)
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        # product_list(Product.title,Product.price)


        if start_price is not None:
            query = query.filter(price__gte=start_price)   #اگر مقدار قیمت بزرگتر یا مساوی مقداری که مشخص کردیم بود

        if end_price is not None:
            query = query.filter(price__lte=end_price)


        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query

class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get("product_favorites")
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        context['banners'] = SiteBanner.objects.filter(is_active=True,position__iexact=SiteBanner.SiteBannerPositions.product_detail)
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()

        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()
        product_detail(loaded_product.title,loaded_product.price)
        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorites"] = product_id
        product_favorite(product.title)
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/components/product_categories_component.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)     #برای annotateمیگه اون دیتایی که داری رو واکشی کن من بقیش برات میاررم و روی ابجیکت اعمال میشه
    context = {
        'brands': product_brands
    }
    return render(request, 'product_module/components/product_brands_component.html', context)
