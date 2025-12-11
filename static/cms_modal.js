// Global CMS Modal Functions
function openCMSModal(title, formHtml, formId, submitUrl, method = 'POST') {
    const modalOverlay = document.getElementById('cmsModalOverlay');
    const modalTitle = document.getElementById('cmsModalTitle');
    const modalBody = document.getElementById('cmsModalBody');
    
    if (!modalOverlay || !modalTitle || !modalBody) {
        console.error('Modal elements not found. Make sure modal_base.html is included.');
        return;
    }
    
    modalTitle.textContent = title;
    modalBody.innerHTML = formHtml;
    modalOverlay.style.display = 'flex';
    
    // Set up form submission
    setTimeout(() => {
        const form = document.getElementById(formId);
        if (form) {
            // Remove existing submit handler
            const newForm = form.cloneNode(true);
            form.parentNode.replaceChild(newForm, form);
            
            // Add new submit handler
            newForm.addEventListener('submit', function(e) {
                e.preventDefault();
                submitCMSForm(newForm, submitUrl, method);
            });
        }
    }, 100);
    
    // Close on overlay click
    modalOverlay.onclick = function(e) {
        if (e.target === modalOverlay) {
            closeCMSModal();
        }
    };
    
    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modalOverlay.style.display === 'flex') {
            closeCMSModal();
        }
    });
}

function closeCMSModal() {
    const modalOverlay = document.getElementById('cmsModalOverlay');
    const modalBody = document.getElementById('cmsModalBody');
    
    if (modalOverlay) {
        modalOverlay.style.display = 'none';
    }
    if (modalBody) {
        modalBody.innerHTML = '';
    }
}

function submitCMSForm(form, url, method = 'POST') {
    const formData = new FormData(form);
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.innerHTML : '';
    
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
    }
    
    fetch(url, {
        method: method,
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification(data.message, 'success');
            closeCMSModal();
            setTimeout(() => location.reload(), 1000);
        } else {
            showNotification('Error: ' + (data.message || 'Please check the form'), 'error');
            if (data.errors) {
                displayFormErrors(form, data.errors);
            }
        }
    })
    .catch(error => {
        showNotification('An error occurred. Please try again.', 'error');
        console.error('Error:', error);
    })
    .finally(() => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
        }
    });
}

function displayFormErrors(form, errors) {
    // Clear previous errors
    form.querySelectorAll('.form-error').forEach(el => el.remove());
    form.querySelectorAll('.form-control').forEach(el => el.style.borderColor = '');
    
    Object.keys(errors).forEach(field => {
        const fieldElement = form.querySelector(`[name="${field}"]`);
        if (fieldElement) {
            fieldElement.style.borderColor = '#dc3545';
            const errorDiv = document.createElement('div');
            errorDiv.className = 'form-error';
            errorDiv.style.cssText = 'color: #dc3545; font-size: 0.875rem; margin-top: 0.25rem;';
            errorDiv.textContent = Array.isArray(errors[field]) ? errors[field][0] : errors[field];
            fieldElement.parentElement.appendChild(errorDiv);
        }
    });
}

function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#44b669' : '#dc3545'};
        color: white;
        border-radius: 10px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        z-index: 10001;
        animation: slideInRight 0.3s ease;
        max-width: 400px;
    `;
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

