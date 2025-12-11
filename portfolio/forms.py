from django import forms
from .models import PortfolioItem, PortfolioCategory


class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['title', 'description', 'short_description', 'featured_image', 
                  'categories', 'client_name', 'project_date', 'project_url', 'is_featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'project_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

