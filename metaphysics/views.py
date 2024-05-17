from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views import View
from .forms import ContactForm
from .models import AboutInfo, Blog, Sign, Service, TeamMember, Slider, Video, Faq, Product, Contacts

# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'metaphysics/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        about_info = AboutInfo.objects.first()
        context["about_info"] = about_info

        blogs = Blog.objects.order_by('-id')[:3]
        context['blogs'] = blogs

        signs = Sign.objects.all()
        context['signs'] = signs

        services = Service.objects.all()
        context['services'] = services

        team_members = TeamMember.objects.all()
        context['team_members'] = team_members

        sliders = Slider.objects.all()
        context['sliders'] = sliders

        return context


class AboutView(TemplateView):
    template_name = 'metaphysics/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        about_info = AboutInfo.objects.first()
        context["about_info"] = about_info

        faqs = Faq.objects.all()
        context['faqs'] = faqs

        return context


class ShopView(ListView):
    model = Product
    template_name = 'metaphysics/shop.html'
    context_object_name = "products"
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.all()


class ProductView(View):
    model = Product
    template_name = 'metaphysics/product_details.html'

    def get(self, request, slug):
        products = Product.objects.order_by('-id')[:4]
        product = Product.objects.get(slug=slug)
        context = {
            "product": product,
            "images": product.images.all(),
            "products": products
        }
        return render(request, 'metaphysics/product_details.html', context)


def articles(request):
    return render(request, 'metaphysics/articles.html')


class BlogsView(ListView):
    model = Blog
    template_name = 'metaphysics/blogs.html'
    context_object_name = "blogs"
    paginate_by = 4


class Contact(View):
    def get(self, request):
        contacts = Contacts.objects.first()
        return render(request, 'metaphysics/contact.html',  context={'form': ContactForm(), 'contacts': contacts})

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            print(contact_form)
            contact_form.save(commit=True)
            return redirect('success-page')
        else:
            return render(request, 'metaphysics/contact.html', {'form': contact_form})


class ServicesView(ListView):
    model = Service
    template_name = 'metaphysics/services.html'
    context_object_name = "services"
    paginate_by = 4

    def get_queryset(self):
        return Service.objects.all()


class ServiceView(View):
    model = Service
    template_name = 'metaphysics/service_details.html'

    def get(self, request, slug):
        services = Service.objects.order_by('-id')[:4]
        service = Service.objects.get(slug=slug)
        context = {
            "service": service,
            "images": service.images.all(),
            "services": services
        }
        return render(request, 'metaphysics/service_details.html', context)


class VideosView(ListView):
    model = Video
    template_name = 'metaphysics/videos.html'
    context_object_name = "videos"
    paginate_by = 4

    def get_queryset(self):
        return Video.objects.all()


def success(request):
    return render(request, 'metaphysics/success.html')
