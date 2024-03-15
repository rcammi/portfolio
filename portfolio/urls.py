from django.urls import path

from . import views

urlpatterns = [
    path("about/", views.home, name='portfolio-home'),
    # path("about/", views.about, name='portfolio-about'),
    path("<int:pk>/", views.full_view, name='portfolio-full_view'),
    path("", views.project_list, name='portfolio-projects'),
    path("blog/", views.blog_list, name="portfolio-blog"),
    path("contact/", views.contact, name="portfolio-contact"),
    path("contact_success/", views.contact, name="contact_success"),
]
