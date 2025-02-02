from typing import Any
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import ProductCommentForm
from .models import Product, ProductComment, Category
# Create your views here.

class ProductList(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 8
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)       
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class SearchResultsView(generic.ListView):
    model = Product
    template_name = 'products/search-product.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        products=Product.objects.filter(Q(title__icontains=query))
        return products  


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'    
    context_object_name = 'product'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['comment'] = ProductCommentForm()

        return context
    
class CommentsView(generic.CreateView):
    model = ProductComment
    form_class = ProductCommentForm 

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, id= product_id)
        obj.product = product

        return super().form_valid(form)

@login_required
def delete_own_comment(request, pk):
    comment = get_object_or_404(ProductComment, pk=pk)
    if comment.user == request.user:
        comment.delete()

    return redirect("product_detail", comment.product.id)
