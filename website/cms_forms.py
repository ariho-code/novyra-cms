"""
Forms for CMS operations
"""
from django import forms
from .models import (
    Feature, ProcessStep, Statistic, TeamMember, Testimonial,
    FAQ, VideoSection, FloatingBackground, NavigationLink
)


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['title', 'description', 'icon', 'image', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': True}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., fas fa-star'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProcessStepForm(forms.ModelForm):
    class Meta:
        model = ProcessStep
        fields = ['title', 'description', 'icon', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': True}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., fas fa-check-circle'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = ['number', 'label', 'icon', 'order', 'is_active']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'e.g., 500+'}),
            'label': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., fas fa-chart-line'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'bio', 'photo', 'email', 'linkedin_url', 'twitter_url', 'order', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/...'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/...'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_position', 'company', 'testimonial_text', 'client_photo', 'rating', 'order', 'is_active']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'client_position': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'testimonial_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
            'client_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'value': 5}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'order', 'is_active']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': True}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class VideoSectionForm(forms.ModelForm):
    class Meta:
        model = VideoSection
        fields = ['title', 'description', 'video_url', 'thumbnail', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'YouTube or Vimeo embed URL'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FloatingBackgroundForm(forms.ModelForm):
    class Meta:
        model = FloatingBackground
        fields = ['name', 'image', 'position', 'animation_speed', 'opacity', 'order', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'animation_speed': forms.Select(attrs={'class': 'form-control'}),
            'opacity': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1, 'min': 0, 'max': 1, 'value': 0.1}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class NavigationLinkForm(forms.ModelForm):
    class Meta:
        model = NavigationLink
        fields = ['title', 'url', 'is_external', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'is_external': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

