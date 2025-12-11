# Homepage Sections CMS Guide

This guide explains all the sections available on the homepage and how to manage them through the CMS.

## All Homepage Sections

The homepage now includes the following sections (all editable from CMS):

### 1. **Header & Navigation**
- **Location**: CMS → Website → Navigation Links
- **What you can edit**: 
  - Add/remove navigation menu items
  - Set custom URLs (internal or external)
  - Reorder menu items
- **Note**: If no custom navigation links are created, default links (Home, About, Services, Portfolio, Blog, Contact) will be shown.

### 2. **Hero Section**
- **Location**: CMS → Website → Homepage Sections → Hero Section
- **What you can edit**:
  - Title and subtitle
  - Background image
  - Background color
  - Content (rich text)
  - Enable/disable section

### 3. **Features / Why Choose Us Section**
- **Location**: CMS → Website → Features
- **What you can edit**:
  - Add multiple feature cards
  - Title, description, icon (Font Awesome class)
  - Optional feature image
  - Reorder features
  - Enable/disable individual features
- **Section Header**: CMS → Website → Homepage Sections → Features Section

### 4. **Services Section**
- **Location**: CMS → Website → Homepage Sections → Services Section
- **What you can edit**:
  - Section title and subtitle
  - Background image/color
  - Enable/disable section
- **Note**: Service cards are hardcoded but link to detailed service pages managed in CMS → Website → Service Pages

### 5. **Process Section**
- **Location**: CMS → Website → Process Steps
- **What you can edit**:
  - Add multiple process steps
  - Title, description, icon
  - Reorder steps (they will be numbered automatically)
  - Enable/disable steps
- **Section Header**: CMS → Website → Homepage Sections → Process Section

### 6. **Statistics Section**
- **Location**: CMS → Website → Statistics
- **What you can edit**:
  - Add multiple statistics
  - Number, label, icon
  - Reorder statistics
  - Enable/disable statistics
- **Section Header**: CMS → Website → Homepage Sections → Statistics Section

### 7. **Portfolio Section**
- **Location**: CMS → Portfolio → Portfolio Items
- **What you can edit**:
  - Add portfolio items
  - Featured image, title, description
  - Mark items as featured (they appear on homepage)
  - Full portfolio management
- **Section Header**: CMS → Website → Homepage Sections → Portfolio Section

### 8. **Team Section**
- **Location**: CMS → Website → Team Members
- **What you can edit**:
  - Add team members
  - Name, position, bio
  - Photo upload
  - Social media links (LinkedIn, Twitter, Email)
  - Reorder team members
  - Enable/disable members
- **Section Header**: CMS → Website → Homepage Sections → Team Section

### 9. **Testimonials Section**
- **Location**: CMS → Website → Testimonials
- **What you can edit**:
  - Add client testimonials
  - Client name, position, company
  - Testimonial text
  - Client photo
  - Rating (1-5 stars)
  - Reorder testimonials
  - Enable/disable testimonials
- **Section Header**: CMS → Website → Homepage Sections → Testimonials Section

### 10. **Consultation Section**
- **Location**: CMS → Website → Consultation Section
- **What you can edit**:
  - Title, subtitle, description
  - Button text
  - Background image
  - Enable/disable section
- **Note**: This is a singleton (only one instance exists)

### 11. **FAQ Section**
- **Location**: CMS → Website → FAQs
- **What you can edit**:
  - Add multiple FAQs
  - Question and answer (rich text)
  - Reorder FAQs
  - Enable/disable FAQs
- **Section Header**: CMS → Website → Homepage Sections → FAQ Section

### 12. **Blog Section**
- **Location**: CMS → Blog → Blog Posts
- **What you can edit**:
  - Create blog posts
  - Featured image, title, content
  - Recent posts automatically appear on homepage
- **Section Header**: CMS → Website → Homepage Sections → Blog Section

### 13. **Contact Section**
- **Location**: CMS → Website → Homepage Sections → Contact Section
- **What you can edit**:
  - Section title and subtitle
  - Contact form is automatically included
  - Contact information comes from Site Settings
- **Note**: Full contact page is managed separately in CMS → Website → Contact Page Content

### 14. **CTA (Call to Action) Section**
- **Location**: CMS → Website → Homepage Sections → CTA Section
- **What you can edit**:
  - Title, subtitle, content (rich text)
  - Background image/color
  - Enable/disable section

### 15. **Footer**
- **Location**: CMS → Website → Footer Content
- **What you can edit**:
  - About text (footer description)
  - Copyright text
  - Newsletter title and text (if needed)
- **Note**: This is a singleton (only one instance exists)
- **Social Media Links**: Managed in CMS → Settings → Site Settings

## Quick Start

1. **Access CMS**: Go to `/cms/admin/` and log in
2. **Manage Sections**: Navigate to "Website" section
3. **Edit Content**: Click on any model to add/edit content
4. **Reorder Items**: Use the "order" field or drag-and-drop in list view
5. **Enable/Disable**: Use the "is_active" checkbox to show/hide items

## Section Ordering

All homepage sections can be reordered using the "order" field in Homepage Sections. Lower numbers appear first.

## Tips

- **Images**: Always upload optimized images for better performance
- **Icons**: Use Font Awesome icon classes (e.g., `fas fa-star`, `fab fa-linkedin-in`)
- **Rich Text**: Use the CKEditor for formatted content in description fields
- **Mobile Responsive**: All sections are automatically mobile-responsive
- **Animations**: Sections use AOS (Animate On Scroll) for smooth animations

## Need Help?

- Check the CMS admin interface for inline help text
- Review the model field descriptions
- Test changes on the homepage after saving

