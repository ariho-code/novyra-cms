from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import PortfolioItem, PortfolioCategory
from .forms import PortfolioItemForm


@login_required
def portfolio_list(request):
    items = PortfolioItem.objects.all().prefetch_related('categories', 'images')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(client_name__icontains=search_query)
        )
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        items = items.filter(categories__id=category_filter)
    
    # Filter featured
    featured_filter = request.GET.get('featured', '')
    if featured_filter == 'true':
        items = items.filter(is_featured=True)
    
    # Pagination
    paginator = Paginator(items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = PortfolioCategory.objects.all()
    
    context = {
        'items': page_obj,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'featured_filter': featured_filter,
    }
    return render(request, 'portfolio/list.html', context)


@login_required
def portfolio_detail(request, slug):
    item = get_object_or_404(PortfolioItem, slug=slug)
    item.views += 1
    item.save(update_fields=['views'])
    return render(request, 'portfolio/detail.html', {'item': item})


@login_required
def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Portfolio item created successfully!')
            return redirect('portfolio:list')
    else:
        form = PortfolioItemForm()
    return render(request, 'portfolio/form.html', {'form': form, 'title': 'Create Portfolio Item'})


@login_required
def portfolio_edit(request, slug):
    item = get_object_or_404(PortfolioItem, slug=slug)
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portfolio item updated successfully!')
            return redirect('portfolio:list')
    else:
        form = PortfolioItemForm(instance=item)
    return render(request, 'portfolio/form.html', {'form': form, 'item': item, 'title': 'Edit Portfolio Item'})


@login_required
def portfolio_delete(request, slug):
    item = get_object_or_404(PortfolioItem, slug=slug)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Portfolio item deleted successfully!')
        return redirect('portfolio:list')
    return render(request, 'portfolio/delete_confirm.html', {'item': item})
