from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from portfolio.models import PortfolioItem
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.db import OperationalError, DatabaseError


@login_required
def dashboard(request):
    # Get statistics with error handling
    try:
        blog_count = BlogPost.objects.count()
    except (OperationalError, DatabaseError):
        blog_count = 0
    except Exception:
        blog_count = 0
    
    try:
        portfolio_count = PortfolioItem.objects.count()
    except (OperationalError, DatabaseError):
        portfolio_count = 0
    except Exception:
        portfolio_count = 0
    
    try:
        user_count = User.objects.count()
    except (OperationalError, DatabaseError):
        user_count = 0
    except Exception:
        user_count = 0
    
    try:
        total_views = BlogPost.objects.aggregate(total=Sum('views'))['total'] or 0
    except (OperationalError, DatabaseError):
        total_views = 0
    except Exception:
        total_views = 0
    
    try:
        portfolio_views = PortfolioItem.objects.aggregate(total=Sum('views'))['total'] or 0
        total_views += portfolio_views
    except (OperationalError, DatabaseError):
        pass
    except Exception:
        pass
    
    # Get recent blog posts
    try:
        recent_posts = BlogPost.objects.select_related('author').prefetch_related('categories')[:5]
    except (OperationalError, DatabaseError):
        recent_posts = []
    except Exception:
        recent_posts = []
    
    context = {
        'blog_count': blog_count,
        'portfolio_count': portfolio_count,
        'user_count': user_count,
        'total_views': total_views,
        'recent_posts': recent_posts,
    }
    return render(request, 'dashboard.html', context)

