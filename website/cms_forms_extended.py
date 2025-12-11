"""
Extended forms for CMS operations
"""
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
    ServicePage, ServiceFeature, AboutPageContent, AboutValue,
    ContactPageContent, FooterContent, ConsultationSection, HomePageSection,
    PricingPackage
)


class ServicePageForm(forms.ModelForm):
    class Meta:
        model = ServicePage
        fields = ['title', 'slug', 'hero_title', 'hero_subtitle', 'hero_background_image', 
                  'intro_text', 'main_content', 'features_title', 'process_title', 
                  'cta_title', 'cta_text', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hero_background_image': forms.FileInput(attrs={'class': 'form-control'}),
            'intro_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'main_content': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
            'features_title': forms.TextInput(attrs={'class': 'form-control'}),
            'process_title': forms.TextInput(attrs={'class': 'form-control'}),
            'cta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'cta_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ServiceFeatureForm(forms.ModelForm):
    class Meta:
        model = ServiceFeature
        fields = ['service', 'title', 'description', 'icon']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': True}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., fas fa-check'}),
        }


class AboutPageContentForm(forms.ModelForm):
    class Meta:
        model = AboutPageContent
        fields = ['hero_title', 'hero_subtitle', 'intro_text', 
                  'mission_title', 'mission_text', 'values_title', 
                  'cta_title', 'cta_text']
        widgets = {
            'hero_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'intro_text': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
            'mission_title': forms.TextInput(attrs={'class': 'form-control'}),
            'mission_text': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
            'values_title': forms.TextInput(attrs={'class': 'form-control'}),
            'cta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'cta_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class AboutValueForm(forms.ModelForm):
    class Meta:
        model = AboutValue
        fields = ['title', 'description', 'icon', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': True}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., fas fa-star'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ContactPageContentForm(forms.ModelForm):
    class Meta:
        model = ContactPageContent
        fields = ['hero_title', 'hero_subtitle', 'address', 
                  'phone', 'business_hours', 'form_title']
        widgets = {
            'hero_title': forms.TextInput(attrs={'class': 'form-control'}),
            'hero_subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'business_hours': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'form_title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FooterContentForm(forms.ModelForm):
    class Meta:
        model = FooterContent
        fields = ['about_text', 'copyright_text']
        widgets = {
            'about_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'copyright_text': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ConsultationSectionForm(forms.ModelForm):
    class Meta:
        model = ConsultationSection
        fields = ['title', 'subtitle', 'description', 'button_text', 'background_image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'description': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
            'button_text': forms.TextInput(attrs={'class': 'form-control'}),
            'background_image': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class HomePageSectionForm(forms.ModelForm):
    class Meta:
        model = HomePageSection
        fields = ['section_type', 'title', 'subtitle', 'content', 
                  'background_image', 'background_color', 'order', 'is_active']
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'content': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
            'background_image': forms.FileInput(attrs={'class': 'form-control'}),
            'background_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PricingPackageForm(forms.ModelForm):
    features = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Enter one feature per line'}),
        help_text='Enter one feature per line'
    )
    
    class Meta:
        model = PricingPackage
        fields = ['name', 'price', 'currency', 'billing_period', 'features', 'is_featured', 'is_active', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'required': True}),
            'currency': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 10}),
            'billing_period': forms.TextInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def clean_features(self):
        """Convert newline-separated features to list"""
        features_text = self.cleaned_data.get('features', '')
        if features_text:
            features = [f.strip() for f in features_text.split('\n') if f.strip()]
            return features
        return []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.features:
            # Convert list to newline-separated string for textarea
            self.initial['features'] = '\n'.join(self.instance.features)
