from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.core.paginator import Paginator
from .models import BlogPost, Category
from .forms import BlogPostForm


@login_required
def blog_list(request):
    posts = BlogPost.objects.all().select_related('author').prefetch_related('categories')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__username__icontains=search_query)
        )
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        posts = posts.filter(status=status_filter)
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        posts = posts.filter(categories__id=category_filter)
    
    # Pagination
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'posts': page_obj,
        'categories': categories,
        'search_query': search_query,
        'status_filter': status_filter,
        'category_filter': category_filter,
    }
    return render(request, 'blog/list.html', context)


@login_required
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog:list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/form.html', {'form': form, 'title': 'Create Blog Post'})


@login_required
def blog_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog:list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/form.html', {'form': form, 'post': post, 'title': 'Edit Blog Post'})


@login_required
def blog_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog:list')
    return render(request, 'blog/delete_confirm.html', {'post': post})
