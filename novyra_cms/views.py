from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from portfolio.models import PortfolioItem
from django.contrib.auth.models import User
from django.db.models import Count, Sum


@login_required
def dashboard(request):
    # Get statistics
    blog_count = BlogPost.objects.count()
    portfolio_count = PortfolioItem.objects.count()
    user_count = User.objects.count()
    total_views = BlogPost.objects.aggregate(total=Sum('views'))['total'] or 0
    total_views += PortfolioItem.objects.aggregate(total=Sum('views'))['total'] or 0
    
    # Get recent blog posts
    recent_posts = BlogPost.objects.select_related('author').prefetch_related('categories')[:5]
    
    context = {
        'blog_count': blog_count,
        'portfolio_count': portfolio_count,
        'user_count': user_count,
        'total_views': total_views,
        'recent_posts': recent_posts,
    }
    return render(request, 'dashboard.html', context)

