from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="main-page"),
    path("about", views.AboutView.as_view(), name="about-page"),
    path("shop/", views.ShopView.as_view(), name="shop-page"),
    path("shop/<slug:slug>", views.ProductView.as_view(), name="product-detail"),
    path("articles", views.articles, name="articles-page"),
    path("services", views.ServicesView.as_view(), name="services-page"),
    path("services/<slug:slug>", views.ServiceView.as_view(), name="service-detail"),
    path("blogs", views.BlogsView.as_view(), name="blogs-page"),
    path("videos", views.VideosView.as_view(), name="videos-page"),
    path("contact/", views.Contact.as_view(), name="contact-page"),
    path('success', views.success, name="success-page")
]
