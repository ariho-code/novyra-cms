"""
Script to initialize default CMS content for the website
Run: python initialize_cms_content.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novyra_cms.settings')
django.setup()

from settings_app.models import SiteSettings
from website.models import (
    HomePageSection, Statistic, ServicePage, ServiceFeature,
    AboutPageContent, AboutValue, ContactPageContent, FloatingBackground,
    Feature, ProcessStep, TeamMember, Testimonial, ConsultationSection,
    FAQ, FooterContent, NavigationLink
)

def initialize_content():
    print("Initializing CMS content...")
    
    # Update Site Settings
    settings = SiteSettings.load()
    settings.admin_email = 'novyramarketingagency@gmail.com'
    settings.address_line_1 = 'Lagos'
    settings.city = 'Lagos'
    settings.state = 'Lagos State'
    settings.country = 'Nigeria'
    if not settings.logo:
        # Logo will be uploaded via admin
        pass
    settings.save()
    print("[OK] Site settings updated")
    
    # Create Homepage Sections
    sections_data = [
        {
            'section_type': 'hero',
            'title': 'Welcome To Novyra Marketing',
            'subtitle': 'Leading digital marketing agency in Nigeria and Africa. We help businesses grow through strategic digital marketing, compelling branding, and results-driven campaigns.',
            'order': 1,
        },
        {
            'section_type': 'features',
            'title': 'Why Choose Us',
            'subtitle': 'What makes us different',
            'order': 2,
        },
        {
            'section_type': 'services',
            'title': 'What We Do',
            'subtitle': 'We offer five key end-to-end solutions to help your business thrive in the digital landscape',
            'order': 3,
        },
        {
            'section_type': 'process',
            'title': 'Our Process',
            'subtitle': 'How we work with you to achieve success',
            'order': 4,
        },
        {
            'section_type': 'stats',
            'title': 'Our Impact',
            'order': 5,
        },
        {
            'section_type': 'portfolio',
            'title': 'Featured Work',
            'subtitle': 'Explore some of our successful projects and campaigns',
            'order': 6,
        },
        {
            'section_type': 'team',
            'title': 'Our Team',
            'subtitle': 'Meet the experts behind Novyra Marketing',
            'order': 7,
        },
        {
            'section_type': 'testimonials',
            'title': 'What Our Clients Say',
            'subtitle': "Don't just take our word for it",
            'order': 8,
        },
        {
            'section_type': 'consultation',
            'title': 'Free Consultation',
            'order': 9,
        },
        {
            'section_type': 'faq',
            'title': 'Frequently Asked Questions',
            'subtitle': 'Everything you need to know',
            'order': 10,
        },
        {
            'section_type': 'blog',
            'title': 'Latest Insights',
            'subtitle': 'Stay updated with our latest marketing tips and strategies',
            'order': 11,
        },
        {
            'section_type': 'contact',
            'title': 'Get In Touch',
            'subtitle': "Let's discuss how we can help grow your business",
            'order': 12,
        },
        {
            'section_type': 'cta',
            'title': 'Ready to Grow Your Business?',
            'subtitle': 'Get started with Novyra Marketing today and see the difference we can make',
            'order': 13,
        },
    ]
    
    for section_data in sections_data:
        section, created = HomePageSection.objects.get_or_create(
            section_type=section_data['section_type'],
            defaults=section_data
        )
        if not created:
            for key, value in section_data.items():
                setattr(section, key, value)
            section.save()
    print("[OK] Homepage sections created")
    
    # Create Statistics
    stats_data = [
        {'number': '500+', 'label': 'Successful Campaigns', 'icon': 'fas fa-bullseye'},
        {'number': '200+', 'label': 'Happy Clients', 'icon': 'fas fa-users'},
        {'number': '15+', 'label': 'Years Experience', 'icon': 'fas fa-calendar'},
        {'number': '98%', 'label': 'Client Satisfaction', 'icon': 'fas fa-star'},
    ]
    
    for stat_data in stats_data:
        stat, created = Statistic.objects.get_or_create(
            number=stat_data['number'],
            defaults=stat_data
        )
    print("[OK] Statistics created")
    
    # Create Service Pages
    services_data = [
        {
            'slug': 'social-media-marketing',
            'title': 'Social Media Marketing',
            'hero_title': 'Social Media Marketing',
            'hero_subtitle': 'Beyond simple posting. Comprehensive social media management that drives results.',
        },
        {
            'slug': 'branding',
            'title': 'Branding',
            'hero_title': 'Branding Services',
            'hero_subtitle': 'Complete brand identity solutions that define and communicate your unique value proposition',
        },
        {
            'slug': 'digital-campaigns',
            'title': 'Digital Campaigns',
            'hero_title': 'Digital Campaigns',
            'hero_subtitle': 'Strategic campaign planning and execution for measurable results',
        },
        {
            'slug': 'content-strategy',
            'title': 'Content Strategy',
            'hero_title': 'Content Strategy',
            'hero_subtitle': 'High-value content that converts visitors into customers',
        },
        {
            'slug': 'advertising',
            'title': 'Paid Advertising',
            'hero_title': 'Paid Advertising (Paid Media)',
            'hero_subtitle': 'Complete paid media management for maximum ROI',
        },
    ]
    
    for service_data in services_data:
        service, created = ServicePage.objects.get_or_create(
            slug=service_data['slug'],
            defaults=service_data
        )
    print("[OK] Service pages created")
    
    # Create About Page Content
    about_content = AboutPageContent.load()
    about_content.hero_title = 'About Novyra Marketing'
    about_content.hero_subtitle = 'Leading digital marketing agency in Nigeria and Africa'
    about_content.intro_text = '<p>At <strong>Novyra Marketing</strong>, we specialize in the <strong>monetization of digital content platforms</strong>. Through a portfolio of niche websites, we connect targeted audiences with valuable information, engaging content, and relevant advertising.</p><p>Whether it\'s through <strong>programmatic ads</strong>, <strong>affiliate marketing</strong>, or <strong>custom partnerships</strong>, we focus on sustainable and ethical growth across all platforms.</p>'
    about_content.mission_title = 'Our Mission'
    about_content.mission_text = '<p>To operate a lean, ethical, and profitable portfolio of websites that serve both readers and advertisers, while staying agile in the fast-changing digital landscape.</p>'
    about_content.save()
    print("[OK] About page content created")
    
    # Create About Values
    values_data = [
        {'title': 'Ad Monetization', 'description': 'We partner with top-tier ad networks to deliver the most relevant and user-friendly ads, maximizing revenue while maintaining user experience.', 'icon': 'fas fa-ad'},
        {'title': 'Affiliate Marketing', 'description': 'By integrating carefully selected affiliate offers, we provide value to our audience while creating sustainable revenue streams.', 'icon': 'fas fa-handshake'},
        {'title': 'Data-Driven', 'description': 'Our strategies are grounded in analytics and optimization to ensure top performance across all platforms and campaigns.', 'icon': 'fas fa-chart-line'},
    ]
    
    for value_data in values_data:
        value, created = AboutValue.objects.get_or_create(
            title=value_data['title'],
            defaults=value_data
        )
    print("[OK] About values created")
    
    # Create Contact Page Content
    contact_content = ContactPageContent.load()
    contact_content.hero_title = 'Contact Us'
    contact_content.hero_subtitle = 'Want to connect with us for a potential partnership, advertising opportunity, or affiliate collaboration?'
    contact_content.address = 'Lagos, Nigeria'
    contact_content.business_hours = 'Monday - Friday: 9:00 AM - 6:00 PM\nSaturday: 10:00 AM - 4:00 PM\nSunday: Closed'
    contact_content.save()
    print("[OK] Contact page content created")
    
    # Create Floating Backgrounds (default gradient circles)
    if not FloatingBackground.objects.exists():
        FloatingBackground.objects.create(
            name='Background Element 1',
            position='top-left',
            animation_speed='slow',
            opacity=0.05
        )
        FloatingBackground.objects.create(
            name='Background Element 2',
            position='top-right',
            animation_speed='medium',
            opacity=0.05
        )
        FloatingBackground.objects.create(
            name='Background Element 3',
            position='bottom-left',
            animation_speed='slow',
            opacity=0.05
        )
        FloatingBackground.objects.create(
            name='Background Element 4',
            position='bottom-right',
            animation_speed='medium',
            opacity=0.05
        )
    print("[OK] Floating backgrounds created")
    
    # Create Features
    features_data = [
        {
            'title': 'Expert Team',
            'description': 'Our team consists of experienced digital marketing professionals who stay ahead of industry trends.',
            'icon': 'fas fa-users',
        },
        {
            'title': 'Proven Results',
            'description': 'We have a track record of delivering measurable results for businesses across various industries.',
            'icon': 'fas fa-chart-line',
        },
        {
            'title': 'Custom Strategies',
            'description': 'Every business is unique. We create tailored marketing strategies that fit your specific needs.',
            'icon': 'fas fa-lightbulb',
        },
        {
            'title': '24/7 Support',
            'description': 'We provide round-the-clock support to ensure your campaigns run smoothly at all times.',
            'icon': 'fas fa-headset',
        },
    ]
    
    for feature_data in features_data:
        feature, created = Feature.objects.get_or_create(
            title=feature_data['title'],
            defaults=feature_data
        )
    print("[OK] Features created")
    
    # Create Process Steps
    process_data = [
        {
            'title': 'Discovery & Strategy',
            'description': 'We start by understanding your business, goals, and target audience to develop a comprehensive strategy.',
            'icon': 'fas fa-search',
            'order': 1,
        },
        {
            'title': 'Planning & Development',
            'description': 'Our team creates detailed plans and develops all necessary assets for your marketing campaigns.',
            'icon': 'fas fa-tasks',
            'order': 2,
        },
        {
            'title': 'Execution & Launch',
            'description': 'We launch your campaigns across all selected platforms and channels with precision and care.',
            'icon': 'fas fa-rocket',
            'order': 3,
        },
        {
            'title': 'Optimization & Growth',
            'description': 'We continuously monitor, analyze, and optimize your campaigns to maximize ROI and drive growth.',
            'icon': 'fas fa-chart-bar',
            'order': 4,
        },
    ]
    
    for process_data_item in process_data:
        process, created = ProcessStep.objects.get_or_create(
            title=process_data_item['title'],
            defaults=process_data_item
        )
    print("[OK] Process steps created")
    
    # Create Consultation Section
    consultation = ConsultationSection.load()
    consultation.title = 'Ready to Grow Your Business?'
    consultation.subtitle = 'Get a free consultation with our marketing experts'
    consultation.description = '<p>Let\'s discuss how we can help you achieve your marketing goals and grow your business.</p>'
    consultation.button_text = 'Get Started'
    consultation.save()
    print("[OK] Consultation section created")
    
    # Create FAQs
    faqs_data = [
        {
            'question': 'What services does Novyra Marketing offer?',
            'answer': '<p>We offer five key end-to-end solutions: Social Media Marketing, Branding, Digital Campaigns, Content Strategy, and Paid Advertising (Paid Media).</p>',
            'order': 1,
        },
        {
            'question': 'How long does it take to see results?',
            'answer': '<p>Results vary depending on the service and campaign type. Typically, you can expect to see initial results within 2-4 weeks, with significant improvements over 3-6 months.</p>',
            'order': 2,
        },
        {
            'question': 'Do you work with businesses of all sizes?',
            'answer': '<p>Yes! We work with startups, small businesses, and large enterprises. Our strategies are tailored to fit your specific needs and budget.</p>',
            'order': 3,
        },
        {
            'question': 'What is your pricing structure?',
            'answer': '<p>Our pricing is customized based on your specific needs and goals. Contact us for a free consultation and personalized quote.</p>',
            'order': 4,
        },
        {
            'question': 'Where is Novyra Marketing based?',
            'answer': '<p>We are based in Lagos, Nigeria, and serve clients across Nigeria and Africa.</p>',
            'order': 5,
        },
    ]
    
    for faq_data in faqs_data:
        faq, created = FAQ.objects.get_or_create(
            question=faq_data['question'],
            defaults=faq_data
        )
    print("[OK] FAQs created")
    
    # Create Footer Content
    footer_content = FooterContent.load()
    footer_content.about_text = 'Leading digital marketing agency in Nigeria and Africa. We help businesses grow through strategic digital marketing, compelling branding, and results-driven campaigns.'
    footer_content.copyright_text = '© 2025 Novyra Marketing. All rights reserved.'
    footer_content.save()
    print("[OK] Footer content created")
    
    # Create Navigation Links (if not exists)
    if not NavigationLink.objects.exists():
        nav_links_data = [
            {'title': 'Home', 'url': '/', 'order': 1},
            {'title': 'About', 'url': '/about/', 'order': 2},
            {'title': 'Services', 'url': '/services/', 'order': 3},
            {'title': 'Portfolio', 'url': '/portfolio/', 'order': 4},
            {'title': 'Blog', 'url': '/blog/', 'order': 5},
            {'title': 'Contact', 'url': '/contact/', 'order': 6},
        ]
        
        for nav_data in nav_links_data:
            NavigationLink.objects.create(**nav_data)
    print("[OK] Navigation links created")
    
    print("\n[SUCCESS] CMS content initialized successfully!")
    print("\nNext steps:")
    print("1. Go to /cms/admin/ and upload the logo in Site Settings")
    print("2. Customize homepage sections, service pages, and other content")
    print("3. Upload floating background images if desired")

if __name__ == '__main__':
    initialize_content()

