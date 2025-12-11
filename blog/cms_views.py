"""
CMS views for blog categories
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from django.db.models import Q
from .models import Category
from .forms import CategoryForm


@login_required
def cms_categories(request):
    """Manage blog categories"""
    categories = Category.objects.all().order_by('name')
    
    # Search
    search = request.GET.get('search', '')
    if search:
        categories = categories.filter(Q(name__icontains=search) | Q(description__icontains=search))
    
    return render(request, 'blog/cms/categories.html', {
        'categories': categories,
        'search': search,
    })


@login_required
@require_http_methods(["POST"])
def cms_category_create(request):
    """Create category via AJAX"""
    form = CategoryForm(request.POST)
    if form.is_valid():
        category = form.save()
        return JsonResponse({
            'success': True,
            'message': 'Category created successfully!',
            'id': category.id
        })
    return JsonResponse({
        'success': False,
        'errors': form.errors
    }, status=400)


@login_required
@require_http_methods(["POST"])
def cms_category_update(request, pk):
    """Update category via AJAX"""
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST, instance=category)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Category updated successfully!'
        })
    return JsonResponse({
        'success': False,
        'errors': form.errors
    }, status=400)


@login_required
@require_http_methods(["POST"])
def cms_category_delete(request, pk):
    """Delete category via AJAX"""
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return JsonResponse({
        'success': True,
        'message': 'Category deleted successfully!'
    })


@login_required
def cms_category_get(request, pk):
    """Get category data for editing"""
    category = get_object_or_404(Category, pk=pk)
    data = model_to_dict(category)
    return JsonResponse(data)

