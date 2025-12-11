"""
Custom CMS views for managing website content
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
from .models import (
    HomePageSection, Feature, ProcessStep, Statistic, TeamMember,
    Testimonial, FAQ, VideoSection, ServicePage, AboutPageContent, AboutValue,
    ContactPageContent, ContactMessage, FloatingBackground,
    NavigationLink, FooterContent, ConsultationSection, PricingPackage
)
from .cms_forms import (
    FeatureForm, ProcessStepForm, StatisticForm, TeamMemberForm,
    TestimonialForm, FAQForm, VideoSectionForm, FloatingBackgroundForm,
    NavigationLinkForm
)
from .cms_forms_extended import (
    ServicePageForm, ServiceFeatureForm, AboutPageContentForm, AboutValueForm,
    ContactPageContentForm, FooterContentForm, ConsultationSectionForm, HomePageSectionForm,
    PricingPackageForm
)


@login_required
def cms_homepage_sections(request):
    """Manage homepage sections"""
    sections = HomePageSection.objects.all().order_by('order')
    return render(request, 'website/cms/homepage_sections.html', {
        'sections': sections,
    })


@login_required
def cms_features(request):
    """Manage features"""
    features = Feature.objects.all().order_by('order')
    
    # Search
    search = request.GET.get('search', '')
    if search:
        features = features.filter(Q(title__icontains=search) | Q(description__icontains=search))
    
    # Pagination
    paginator = Paginator(features, 12)
    page = request.GET.get('page')
    features = paginator.get_page(page)
    
    return render(request, 'website/cms/features.html', {
        'features': features,
        'search': search,
    })


@login_required
def cms_process_steps(request):
    """Manage process steps"""
    steps = ProcessStep.objects.all().order_by('order')
    return render(request, 'website/cms/process_steps.html', {
        'steps': steps,
    })


@login_required
def cms_statistics(request):
    """Manage statistics"""
    stats = Statistic.objects.all().order_by('order')
    return render(request, 'website/cms/statistics.html', {
        'stats': stats,
    })


@login_required
def cms_team_members(request):
    """Manage team members"""
    members = TeamMember.objects.all().order_by('order')
    
    # Search
    search = request.GET.get('search', '')
    if search:
        members = members.filter(Q(name__icontains=search) | Q(position__icontains=search))
    
    # Pagination
    paginator = Paginator(members, 12)
    page = request.GET.get('page')
    members = paginator.get_page(page)
    
    return render(request, 'website/cms/team_members.html', {
        'members': members,
        'search': search,
    })


@login_required
def cms_testimonials(request):
    """Manage testimonials"""
    testimonials = Testimonial.objects.all().order_by('order')
    
    # Search
    search = request.GET.get('search', '')
    if search:
        testimonials = testimonials.filter(
            Q(client_name__icontains=search) |
            Q(company__icontains=search) |
            Q(testimonial_text__icontains=search)
        )
    
    # Pagination
    paginator = Paginator(testimonials, 12)
    page = request.GET.get('page')
    testimonials = paginator.get_page(page)
    
    return render(request, 'website/cms/testimonials.html', {
        'testimonials': testimonials,
        'search': search,
    })


@login_required
def cms_faqs(request):
    """Manage FAQs"""
    faqs = FAQ.objects.all().order_by('order')
    
    # Search
    search = request.GET.get('search', '')
    if search:
        faqs = faqs.filter(Q(question__icontains=search) | Q(answer__icontains=search))
    
    # Pagination
    paginator = Paginator(faqs, 12)
    page = request.GET.get('page')
    faqs = paginator.get_page(page)
    
    return render(request, 'website/cms/faqs.html', {
        'faqs': faqs,
        'search': search,
    })


@login_required
def cms_videos(request):
    """Manage videos"""
    videos = VideoSection.objects.all().order_by('order')
    return render(request, 'website/cms/videos.html', {
        'videos': videos,
    })


@login_required
def cms_contact_messages(request):
    """View contact messages"""
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    
    # Filter by read status
    filter_status = request.GET.get('filter', 'all')
    if filter_status == 'unread':
        messages_list = messages_list.filter(is_read=False)
    elif filter_status == 'read':
        messages_list = messages_list.filter(is_read=True)
    
    # Search
    search = request.GET.get('search', '')
    if search:
        messages_list = messages_list.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(subject__icontains=search) |
            Q(message__icontains=search)
        )
    
    # Pagination
    paginator = Paginator(messages_list, 20)
    page = request.GET.get('page')
    messages_list = paginator.get_page(page)
    
    return render(request, 'website/cms/contact_messages.html', {
        'messages_list': messages_list,
        'search': search,
        'filter_status': filter_status,
    })


@login_required
def cms_contact_message_detail(request, message_id):
    """View contact message detail"""
    message = get_object_or_404(ContactMessage, id=message_id)
    
    # Mark as read
    if not message.is_read:
        message.is_read = True
        message.save()
    
    return render(request, 'website/cms/contact_message_detail.html', {
        'message': message,
    })


@login_required
def cms_service_pages(request):
    """Manage service pages"""
    services = ServicePage.objects.all().order_by('title')
    
    # Search
    search = request.GET.get('search', '')
    if search:
        services = services.filter(Q(title__icontains=search) | Q(slug__icontains=search))
    
    return render(request, 'website/cms/service_pages.html', {
        'services': services,
        'search': search,
    })


# Service Page AJAX views
@login_required
@require_http_methods(["POST"])
def cms_service_create(request):
    form = ServicePageForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Service page created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_service_update(request, pk):
    obj = get_object_or_404(ServicePage, pk=pk)
    form = ServicePageForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Service page updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_service_delete(request, pk):
    obj = get_object_or_404(ServicePage, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Service page deleted successfully!'})

@login_required
def cms_service_get(request, pk):
    obj = get_object_or_404(ServicePage, pk=pk)
    data = model_to_dict(obj)
    if obj.hero_background_image:
        data['hero_background_image_url'] = obj.hero_background_image.url
    return JsonResponse(data)


# About Page CMS views
@login_required
def cms_about_page(request):
    """Manage about page content"""
    about_content = AboutPageContent.load()
    return render(request, 'website/cms/about_page.html', {
        'about_content': about_content,
    })

@login_required
@require_http_methods(["POST"])
def cms_about_update(request):
    about_content = AboutPageContent.load()
    form = AboutPageContentForm(request.POST, request.FILES, instance=about_content)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'About page updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
def cms_about_values(request):
    """Manage about values"""
    values = AboutValue.objects.all().order_by('order')
    return render(request, 'website/cms/about_values.html', {
        'values': values,
    })

@login_required
@require_http_methods(["POST"])
def cms_about_value_create(request):
    form = AboutValueForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Value created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_about_value_update(request, pk):
    obj = get_object_or_404(AboutValue, pk=pk)
    form = AboutValueForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Value updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_about_value_delete(request, pk):
    obj = get_object_or_404(AboutValue, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Value deleted successfully!'})

@login_required
def cms_about_value_get(request, pk):
    obj = get_object_or_404(AboutValue, pk=pk)
    data = model_to_dict(obj)
    return JsonResponse(data)


# Contact Page CMS views
@login_required
def cms_contact_page(request):
    """Manage contact page content"""
    contact_content = ContactPageContent.load()
    return render(request, 'website/cms/contact_page.html', {
        'contact_content': contact_content,
    })

@login_required
@require_http_methods(["POST"])
def cms_contact_update(request):
    contact_content = ContactPageContent.load()
    form = ContactPageContentForm(request.POST, request.FILES, instance=contact_content)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Contact page updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)


# Footer CMS views
@login_required
def cms_footer(request):
    """Manage footer content"""
    footer_content = FooterContent.load()
    return render(request, 'website/cms/footer.html', {
        'footer_content': footer_content,
    })

@login_required
@require_http_methods(["POST"])
def cms_footer_update(request):
    footer_content = FooterContent.load()
    form = FooterContentForm(request.POST, instance=footer_content)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Footer updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)


# Consultation Section CMS views
@login_required
def cms_consultation(request):
    """Manage consultation section"""
    consultation = ConsultationSection.load()
    return render(request, 'website/cms/consultation.html', {
        'consultation': consultation,
    })

@login_required
@require_http_methods(["POST"])
def cms_consultation_update(request):
    consultation = ConsultationSection.load()
    form = ConsultationSectionForm(request.POST, request.FILES, instance=consultation)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Consultation section updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)


# Pricing Packages CMS views
@login_required
def cms_pricing_packages(request):
    """Manage pricing packages"""
    packages = PricingPackage.objects.all().order_by('order', 'price')
    
    # Search
    search = request.GET.get('search', '')
    if search:
        packages = packages.filter(Q(name__icontains=search))
    
    return render(request, 'website/cms/pricing_packages.html', {
        'packages': packages,
        'search': search,
    })

@login_required
@require_http_methods(["POST"])
def cms_pricing_create(request):
    form = PricingPackageForm(request.POST)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Pricing package created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_pricing_update(request, pk):
    obj = get_object_or_404(PricingPackage, pk=pk)
    form = PricingPackageForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Pricing package updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_pricing_delete(request, pk):
    obj = get_object_or_404(PricingPackage, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Pricing package deleted successfully!'})

@login_required
def cms_pricing_get(request, pk):
    obj = get_object_or_404(PricingPackage, pk=pk)
    data = model_to_dict(obj)
    # Convert features list to newline-separated string
    if data.get('features'):
        data['features_text'] = '\n'.join(data['features'])
    return JsonResponse(data)


@login_required
def cms_floating_backgrounds(request):
    """Manage floating backgrounds"""
    backgrounds = FloatingBackground.objects.all().order_by('order')
    return render(request, 'website/cms/floating_backgrounds.html', {
        'backgrounds': backgrounds,
    })


@login_required
def cms_navigation_links(request):
    """Manage navigation links"""
    links = NavigationLink.objects.all().order_by('order')
    return render(request, 'website/cms/navigation_links.html', {
        'links': links,
    })


# AJAX Views for CRUD operations
@login_required
@require_http_methods(["POST"])
def cms_feature_create(request):
    """Create feature via AJAX"""
    form = FeatureForm(request.POST, request.FILES)
    if form.is_valid():
        feature = form.save()
        return JsonResponse({
            'success': True,
            'message': 'Feature created successfully!',
            'id': feature.id
        })
    return JsonResponse({
        'success': False,
        'errors': form.errors
    }, status=400)


@login_required
@require_http_methods(["POST"])
def cms_feature_update(request, pk):
    """Update feature via AJAX"""
    feature = get_object_or_404(Feature, pk=pk)
    form = FeatureForm(request.POST, request.FILES, instance=feature)
    if form.is_valid():
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Feature updated successfully!'
        })
    return JsonResponse({
        'success': False,
        'errors': form.errors
    }, status=400)


@login_required
@require_http_methods(["POST"])
def cms_feature_delete(request, pk):
    """Delete feature via AJAX"""
    feature = get_object_or_404(Feature, pk=pk)
    feature.delete()
    return JsonResponse({
        'success': True,
        'message': 'Feature deleted successfully!'
    })


@login_required
def cms_feature_get(request, pk):
    """Get feature data for editing"""
    feature = get_object_or_404(Feature, pk=pk)
    data = model_to_dict(feature)
    if feature.image:
        data['image_url'] = feature.image.url
    return JsonResponse(data)


# Process Step AJAX views
@login_required
@require_http_methods(["POST"])
def cms_process_create(request):
    form = ProcessStepForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Process Step created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_process_update(request, pk):
    obj = get_object_or_404(ProcessStep, pk=pk)
    form = ProcessStepForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Process Step updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_process_delete(request, pk):
    obj = get_object_or_404(ProcessStep, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Process Step deleted successfully!'})

@login_required
def cms_process_get(request, pk):
    obj = get_object_or_404(ProcessStep, pk=pk)
    data = model_to_dict(obj)
    return JsonResponse(data)

# Statistic AJAX views
@login_required
@require_http_methods(["POST"])
def cms_statistic_create(request):
    form = StatisticForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Statistic created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_statistic_update(request, pk):
    obj = get_object_or_404(Statistic, pk=pk)
    form = StatisticForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Statistic updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_statistic_delete(request, pk):
    obj = get_object_or_404(Statistic, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Statistic deleted successfully!'})

@login_required
def cms_statistic_get(request, pk):
    obj = get_object_or_404(Statistic, pk=pk)
    data = model_to_dict(obj)
    return JsonResponse(data)

# Team Member AJAX views
@login_required
@require_http_methods(["POST"])
def cms_team_create(request):
    form = TeamMemberForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Team Member created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_team_update(request, pk):
    obj = get_object_or_404(TeamMember, pk=pk)
    form = TeamMemberForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Team Member updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_team_delete(request, pk):
    obj = get_object_or_404(TeamMember, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Team Member deleted successfully!'})

@login_required
def cms_team_get(request, pk):
    obj = get_object_or_404(TeamMember, pk=pk)
    data = model_to_dict(obj)
    if obj.photo:
        data['photo_url'] = obj.photo.url
    return JsonResponse(data)

# Testimonial AJAX views
@login_required
@require_http_methods(["POST"])
def cms_testimonial_create(request):
    form = TestimonialForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Testimonial created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_testimonial_update(request, pk):
    obj = get_object_or_404(Testimonial, pk=pk)
    form = TestimonialForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Testimonial updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_testimonial_delete(request, pk):
    obj = get_object_or_404(Testimonial, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Testimonial deleted successfully!'})

@login_required
def cms_testimonial_get(request, pk):
    obj = get_object_or_404(Testimonial, pk=pk)
    data = model_to_dict(obj)
    if obj.client_photo:
        data['client_photo_url'] = obj.client_photo.url
    return JsonResponse(data)

# FAQ AJAX views
@login_required
@require_http_methods(["POST"])
def cms_faq_create(request):
    form = FAQForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'FAQ created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_faq_update(request, pk):
    obj = get_object_or_404(FAQ, pk=pk)
    form = FAQForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'FAQ updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_faq_delete(request, pk):
    obj = get_object_or_404(FAQ, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'FAQ deleted successfully!'})

@login_required
def cms_faq_get(request, pk):
    obj = get_object_or_404(FAQ, pk=pk)
    data = model_to_dict(obj)
    return JsonResponse(data)

# Video Section AJAX views
@login_required
@require_http_methods(["POST"])
def cms_video_create(request):
    form = VideoSectionForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Video created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_video_update(request, pk):
    obj = get_object_or_404(VideoSection, pk=pk)
    form = VideoSectionForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Video updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_video_delete(request, pk):
    obj = get_object_or_404(VideoSection, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Video deleted successfully!'})

@login_required
def cms_video_get(request, pk):
    obj = get_object_or_404(VideoSection, pk=pk)
    data = model_to_dict(obj)
    if obj.thumbnail:
        data['thumbnail_url'] = obj.thumbnail.url
    return JsonResponse(data)

# Floating Background AJAX views
@login_required
@require_http_methods(["POST"])
def cms_background_create(request):
    form = FloatingBackgroundForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Floating Background created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_background_update(request, pk):
    obj = get_object_or_404(FloatingBackground, pk=pk)
    form = FloatingBackgroundForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Floating Background updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_background_delete(request, pk):
    obj = get_object_or_404(FloatingBackground, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Floating Background deleted successfully!'})

@login_required
def cms_background_get(request, pk):
    obj = get_object_or_404(FloatingBackground, pk=pk)
    data = model_to_dict(obj)
    if obj.image:
        data['image_url'] = obj.image.url
    return JsonResponse(data)

# Navigation Link AJAX views
@login_required
@require_http_methods(["POST"])
def cms_navlink_create(request):
    form = NavigationLinkForm(request.POST, request.FILES)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({'success': True, 'message': 'Navigation Link created successfully!', 'id': obj.id})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_navlink_update(request, pk):
    obj = get_object_or_404(NavigationLink, pk=pk)
    form = NavigationLinkForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Navigation Link updated successfully!'})
    return JsonResponse({'success': False, 'errors': form.errors}, status=400)

@login_required
@require_http_methods(["POST"])
def cms_navlink_delete(request, pk):
    obj = get_object_or_404(NavigationLink, pk=pk)
    obj.delete()
    return JsonResponse({'success': True, 'message': 'Navigation Link deleted successfully!'})

@login_required
def cms_navlink_get(request, pk):
    obj = get_object_or_404(NavigationLink, pk=pk)
    data = model_to_dict(obj)
    return JsonResponse(data)

