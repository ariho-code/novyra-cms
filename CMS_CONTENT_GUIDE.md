# 🎛️ CMS Content Management Guide

## Overview

**Everything on the website is now editable from the CMS!** All content, images, banners, backgrounds, and settings can be managed through the admin panel.

## Accessing the CMS

1. Go to: http://127.0.0.1:8000/cms/admin/
2. Login with your admin credentials
3. Navigate to different sections to edit content

## What Can Be Edited

### 1. Site Settings (`Settings App > Site Settings`)
- **Logo**: Upload your logo (appears in navbar and browser tab)
- **Favicon**: Upload favicon for browser tab
- **Email**: novyramarketingagency@gmail.com (already set)
- **Address**: Lagos, Nigeria (already set)
- **Phone**: Add phone number
- **Social Media Links**: Facebook, Twitter, Instagram, LinkedIn
- **SEO Settings**: Meta title, description, keywords

### 2. Homepage Sections (`Website > Homepage Sections`)
- **Hero Section**: Title, subtitle, content, background image
- **Services Section**: Title and subtitle
- **Statistics Section**: Title
- **Portfolio Section**: Title and subtitle
- **Blog Section**: Title and subtitle
- **CTA Section**: Call-to-action content

### 3. Statistics (`Website > Statistics`)
- Add/edit statistics that appear on homepage
- Each stat has: Number, Label, Icon (Font Awesome class), Order
- Example: "500+" - "Successful Campaigns" with icon `fas fa-bullseye`

### 4. Service Pages (`Website > Service Pages`)
- **5 Service Pages** already created:
  - Social Media Marketing
  - Branding
  - Digital Campaigns
  - Content Strategy
  - Paid Advertising

- For each service page you can edit:
  - Hero title and subtitle
  - Hero background image
  - Intro text (rich text editor)
  - Main content (rich text editor)
  - Features (add multiple features with icons)
  - CTA title and text

### 5. About Page (`Website > About Page Contents`)
- Hero title and subtitle
- Intro text (rich text editor)
- Mission title and text
- Values title
- CTA title and text

### 6. About Values (`Website > About Values`)
- Add/edit values that appear on about page
- Each value has: Title, Description, Icon, Order

### 7. Contact Page (`Website > Contact Page Contents`)
- Hero title and subtitle
- Address
- Phone number
- Business hours
- Form title

### 8. Floating Backgrounds (`Website > Floating Backgrounds`)
- Add floating/animating background elements
- Upload images or use gradient circles
- Control position, animation speed, opacity
- Multiple backgrounds can be active at once

## How to Edit Content

### Editing Text Content

1. Go to the relevant section in admin
2. Click on the item you want to edit
3. Use the rich text editor (CKEditor) for formatted content
4. Click "Save"

### Uploading Images

1. Click "Choose File" next to image fields
2. Select your image
3. Click "Save"
4. Images are automatically optimized and stored

### Adding Features to Service Pages

1. Go to `Website > Service Pages`
2. Click on a service page
3. Scroll to "Features" section at bottom
4. Click "Add another Service Feature"
5. Fill in: Title, Description, Icon (Font Awesome class)
6. Click "Save"

### Managing Statistics

1. Go to `Website > Statistics`
2. Click "Add Statistic" or edit existing
3. Fill in: Number, Label, Icon, Order
4. Toggle "Is active" to show/hide
5. Click "Save"

## Logo Setup

The logo has been automatically uploaded! It appears in:
- Navigation bar
- Browser tab (favicon)
- All pages

To change the logo:
1. Go to `Settings App > Site Settings`
2. Click on "Site Settings"
3. Scroll to "Logo" field
4. Upload new logo
5. Click "Save"

## Floating Backgrounds

Floating backgrounds add a premium, animated effect to pages.

### Default Backgrounds
- 4 default gradient circles are already created
- They float slowly in different positions
- Low opacity (0.05) for subtle effect

### Adding Custom Backgrounds

1. Go to `Website > Floating Backgrounds`
2. Click "Add Floating Background"
3. Fill in:
   - **Name**: Descriptive name
   - **Image**: Upload your image (optional - uses gradient if not provided)
   - **Animation Speed**: Slow, Medium, or Fast
   - **Position**: Top Left, Top Right, Bottom Left, Bottom Right, or Center
   - **Opacity**: 0.0 to 1.0 (lower = more subtle)
4. Click "Save"

### Tips for Floating Backgrounds
- Use low opacity (0.05-0.15) for subtle effects
- Mix different speeds for dynamic feel
- Use brand colors in gradients
- Don't overdo it - 2-4 backgrounds is usually enough

## Rich Text Editor (CKEditor)

The rich text editor allows you to:
- Format text (bold, italic, headings)
- Add links
- Insert images
- Create lists
- Add tables
- And more!

Just click the formatting buttons in the editor toolbar.

## Best Practices

1. **Always preview changes** - Check the public website after editing
2. **Use consistent formatting** - Keep headings, fonts, and styles consistent
3. **Optimize images** - Compress images before uploading for faster loading
4. **Test on mobile** - Check how changes look on mobile devices
5. **Save frequently** - Don't lose your work!

## Quick Reference

| Content Type | Location in Admin |
|-------------|------------------|
| Logo & Site Info | Settings App > Site Settings |
| Homepage Hero | Website > Homepage Sections (Hero) |
| Statistics | Website > Statistics |
| Service Pages | Website > Service Pages |
| About Page | Website > About Page Contents |
| Contact Page | Website > Contact Page Contents |
| Floating Backgrounds | Website > Floating Backgrounds |
| Blog Posts | Blog > Blog Posts |
| Portfolio Items | Portfolio > Portfolio Items |

## Need Help?

- Check the main README.md for general setup
- All content is now CMS-controlled - no code changes needed!
- Just edit through the admin panel and changes appear immediately

---

**Remember**: Everything is editable from the CMS. No coding required! 🎉

