from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.db import OperationalError, DatabaseError
from blog.models import BlogPost, Category
from portfolio.models import PortfolioItem, PortfolioCategory
from settings_app.models import SiteSettings
from .models import (
    HomePageSection, Statistic, ServicePage, AboutPageContent,
    AboutValue, ContactPageContent, FloatingBackground, Feature,
    ProcessStep, TeamMember, Testimonial, ConsultationSection,
    FAQ, FooterContent, NavigationLink, VideoSection, ContactMessage,
    PricingPackage
)


def home(request):
    """Homepage with hero section and services overview"""
    try:
        recent_posts = BlogPost.objects.filter(status='published').select_related('author')[:3]
    except (OperationalError, DatabaseError):
        recent_posts = []
    except Exception:
        recent_posts = []
    
    try:
        featured_portfolio = PortfolioItem.objects.filter(is_featured=True)[:6]
    except (OperationalError, DatabaseError):
        featured_portfolio = []
    except Exception:
        featured_portfolio = []
    
    try:
        site_settings = SiteSettings.load()
    except (OperationalError, DatabaseError):
        site_settings = None
    except Exception:
        site_settings = None
    
    # Safely load all data with error handling
    try:
        homepage_sections = list(HomePageSection.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        homepage_sections = []
    except Exception:
        homepage_sections = []
    
    try:
        statistics = list(Statistic.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        statistics = []
    except Exception:
        statistics = []
    
    try:
        floating_backgrounds = list(FloatingBackground.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        floating_backgrounds = []
    except Exception:
        floating_backgrounds = []
    
    try:
        features = list(Feature.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        features = []
    except Exception:
        features = []
    
    try:
        process_steps = list(ProcessStep.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        process_steps = []
    except Exception:
        process_steps = []
    
    try:
        team_members = list(TeamMember.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        team_members = []
    except Exception:
        team_members = []
    
    try:
        testimonials = list(Testimonial.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        testimonials = []
    except Exception:
        testimonials = []
    
    try:
        if ConsultationSection.objects.exists():
            consultation = ConsultationSection.load()
        else:
            consultation = None
    except (OperationalError, DatabaseError):
        consultation = None
    except Exception:
        consultation = None
    
    try:
        faqs = list(FAQ.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        faqs = []
    except Exception:
        faqs = []
    
    try:
        if FooterContent.objects.exists():
            footer_content = FooterContent.load()
        else:
            footer_content = None
    except (OperationalError, DatabaseError):
        footer_content = None
    except Exception:
        footer_content = None
    
    try:
        videos = list(VideoSection.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        videos = []
    except Exception:
        videos = []
    
    try:
        pricing_packages = list(PricingPackage.objects.filter(is_active=True).order_by('order', 'price'))
    except (OperationalError, DatabaseError):
        pricing_packages = []
    except Exception:
        pricing_packages = []
    
    context = {
        'recent_posts': recent_posts,
        'featured_portfolio': featured_portfolio,
        'site_settings': site_settings,
        'homepage_sections': homepage_sections,
        'statistics': statistics,
        'floating_backgrounds': floating_backgrounds,
        'features': features,
        'process_steps': process_steps,
        'team_members': team_members,
        'testimonials': testimonials,
        'consultation': consultation,
        'faqs': faqs,
        'footer_content': footer_content,
        'videos': videos,
        'pricing_packages': pricing_packages,
    }
    return render(request, 'website/home.html', context)


def about(request):
    """About page"""
    try:
        site_settings = SiteSettings.load()
    except (OperationalError, DatabaseError):
        site_settings = None
    except Exception:
        site_settings = None
    
    try:
        about_content = AboutPageContent.load()
    except (OperationalError, DatabaseError):
        about_content = None
    except Exception:
        about_content = None
    
    try:
        about_values = list(AboutValue.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        about_values = []
    except Exception:
        about_values = []
    
    try:
        floating_backgrounds = list(FloatingBackground.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        floating_backgrounds = []
    except Exception:
        floating_backgrounds = []
    
    return render(request, 'website/about.html', {
        'site_settings': site_settings,
        'about_content': about_content,
        'about_values': about_values,
        'floating_backgrounds': floating_backgrounds,
    })


def services(request):
    """Services overview page"""
    return render(request, 'website/services.html')


def service_detail(request, service_slug):
    """Individual service detail pages"""
    try:
        service = ServicePage.objects.get(slug=service_slug, is_active=True)
    except (OperationalError, DatabaseError):
        service = None
    except ServicePage.DoesNotExist:
        service = None
    except Exception:
        service = None
    
    try:
        floating_backgrounds = list(FloatingBackground.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        floating_backgrounds = []
    except Exception:
        floating_backgrounds = []
    
    if service:
        return render(request, 'website/service_detail.html', {
            'service': service,
            'floating_backgrounds': floating_backgrounds,
        })
    else:
        # Fallback to old template system
        service_map = {
            'social-media-marketing': 'social_media',
            'branding': 'branding',
            'digital-campaigns': 'digital_campaigns',
            'content-strategy': 'content_strategy',
            'advertising': 'advertising',
        }
        service_type = service_map.get(service_slug)
        if not service_type:
            return render(request, 'website/404.html', status=404)
        return render(request, f'website/services/{service_slug}.html', {
            'service_type': service_type,
            'service_slug': service_slug,
        })


def blog_list(request):
    """Public blog listing page"""
    try:
        posts = BlogPost.objects.filter(status='published').select_related('author').prefetch_related('categories')
    except (OperationalError, DatabaseError):
        posts = BlogPost.objects.none()
    except Exception:
        posts = BlogPost.objects.none()
    
    try:
        site_settings = SiteSettings.load()
    except (OperationalError, DatabaseError):
        site_settings = None
    except Exception:
        site_settings = None
    
    try:
        floating_backgrounds = list(FloatingBackground.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        floating_backgrounds = []
    except Exception:
        floating_backgrounds = []
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query)
        )
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        posts = posts.filter(categories__slug=category_filter)
    
    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    try:
        categories = Category.objects.all()
    except (OperationalError, DatabaseError):
        categories = []
    except Exception:
        categories = []
    
    context = {
        'posts': page_obj,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'site_settings': site_settings,
        'floating_backgrounds': floating_backgrounds,
    }
    return render(request, 'website/blog_list.html', context)


def blog_detail(request, slug):
    """Public blog post detail page"""
    try:
        post = get_object_or_404(BlogPost, slug=slug, status='published')
        post.views += 1
        post.save(update_fields=['views'])
    except (OperationalError, DatabaseError):
        from django.http import Http404
        raise Http404("Blog post not found")
    except Exception:
        from django.http import Http404
        raise Http404("Blog post not found")
    
    # Get related posts
    try:
        related_posts = BlogPost.objects.filter(
            status='published',
            categories__in=post.categories.all()
        ).exclude(id=post.id).distinct()[:3]
    except (OperationalError, DatabaseError):
        related_posts = []
    except Exception:
        related_posts = []
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'website/blog_detail.html', context)


def portfolio_list(request):
    """Public portfolio gallery page"""
    try:
        items = PortfolioItem.objects.all().prefetch_related('categories', 'images')
    except (OperationalError, DatabaseError):
        items = PortfolioItem.objects.none()
    except Exception:
        items = PortfolioItem.objects.none()
    
    try:
        site_settings = SiteSettings.load()
    except (OperationalError, DatabaseError):
        site_settings = None
    except Exception:
        site_settings = None
    
    try:
        floating_backgrounds = list(FloatingBackground.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        floating_backgrounds = []
    except Exception:
        floating_backgrounds = []
    
    # Filter by category
    category_filter = request.GET.get('category', '')
    if category_filter:
        items = items.filter(categories__slug=category_filter)
    
    # Pagination
    paginator = Paginator(items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    try:
        categories = PortfolioCategory.objects.all()
    except (OperationalError, DatabaseError):
        categories = []
    except Exception:
        categories = []
    
    context = {
        'items': page_obj,
        'categories': categories,
        'category_filter': category_filter,
        'site_settings': site_settings,
        'floating_backgrounds': floating_backgrounds,
    }
    return render(request, 'website/portfolio_list.html', context)


def portfolio_detail(request, slug):
    """Public portfolio item detail page"""
    try:
        item = get_object_or_404(PortfolioItem, slug=slug)
        item.views += 1
        item.save(update_fields=['views'])
    except (OperationalError, DatabaseError):
        from django.http import Http404
        raise Http404("Portfolio item not found")
    except Exception:
        from django.http import Http404
        raise Http404("Portfolio item not found")
    
    # Get related items
    try:
        related_items = PortfolioItem.objects.filter(
            categories__in=item.categories.all()
        ).exclude(id=item.id).distinct()[:3]
    except (OperationalError, DatabaseError):
        related_items = []
    except Exception:
        related_items = []
    
    context = {
        'item': item,
        'related_items': related_items,
    }
    return render(request, 'website/portfolio_detail.html', context)


def contact(request):
    """Contact page"""
    try:
        site_settings = SiteSettings.load()
    except (OperationalError, DatabaseError):
        site_settings = None
    except Exception:
        site_settings = None
    
    try:
        contact_content = ContactPageContent.load()
    except (OperationalError, DatabaseError):
        contact_content = None
    except Exception:
        contact_content = None
    
    try:
        floating_backgrounds = list(FloatingBackground.objects.filter(is_active=True))
    except (OperationalError, DatabaseError):
        floating_backgrounds = []
    except Exception:
        floating_backgrounds = []
    
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', 'Contact Form Submission')
        message = request.POST.get('message')
        phone = request.POST.get('phone', '')
        
        # Save to database
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
                phone=phone
            )
            from django.contrib import messages
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
        except (OperationalError, DatabaseError):
            from django.contrib import messages
            messages.error(request, 'Sorry, there was an error saving your message. Please try again later.')
        except Exception:
            from django.contrib import messages
            messages.error(request, 'Sorry, there was an error saving your message. Please try again later.')
        
        return redirect('website:contact')
    
    return render(request, 'website/contact.html', {
        'site_settings': site_settings,
        'contact_content': contact_content,
        'floating_backgrounds': floating_backgrounds,
    })
