from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm
from .models import Blogs, Projects


def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html') #, {'title':'About'}

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],  # subject
                f"Message from {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
                f"{form.cleaned_data['message']}",  # message
                None,  # from email
                ['your-email@example.com'],  # replace with your email
            )
            return render(request, 'portfolio/contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form})

def project_list(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/projects.html', context)

def blog_list(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'portfolio/blog.html', context)

def full_view(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio/full_view.html', context)