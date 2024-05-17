from typing import Any, Iterable
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to="sliders", null=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.ImageField(upload_to="services", null=True)
    title = models.CharField(max_length=50)
    subtitle = models.TextField(max_length=400, null=True)
    slug = models.SlugField(unique=True, max_length=150)
    contact_number = models.CharField(max_length=16, validators=[RegexValidator(
        regex='\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Nömrə düzgün formatda deyil")
    ])

    def __str__(self):
        return self.title


class ServiceImages(models.Model):
    image = models.ImageField(upload_to="services", null=True)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, null=True, related_name="images")

    def __str__(self):
        return f"Image for {self.service.title}"

    class Meta:
        verbose_name_plural = "Service Images"


class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="team_members", null=True)
    duty = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class AboutInfo(models.Model):
    top_image = models.ImageField(upload_to="about", null=True)
    bottom_image = models.ImageField(upload_to="about", null=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    video_url = models.CharField(max_length=200)

    def save(self, force_insert: bool = False, force_update: bool = False, using: str | None = None, update_fields: Iterable[str] | None = None):
        if not self.pk and AboutInfo.objects.exists():
            raise ValidationError("Only one instance of About Info is allowed")
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Info"


class BlogCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blog Categories"


class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length=3000)
    slug = models.SlugField(max_length=150, unique=True)
    image = models.ImageField(upload_to="blogs", null=True)
    category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self):
        return self.title


class BlogImages(models.Model):
    image = models.ImageField(upload_to="blogs", null=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="images")


class Contacts(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    youtube = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    tiktok = models.CharField(max_length=300, blank=True, null=True)
    twitter = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=1000, null=True)
    email = models.EmailField(blank=True, null=True)
    whatsapp = models.CharField(max_length=16, blank=True, null=True, validators=[RegexValidator(
        regex='\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Nömrə düzgün formatda deyil")
    ])
    phone = models.CharField(max_length=16, blank=True, null=True, validators=[RegexValidator(
        regex='\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Nömrə düzgün formatda deyil")
    ])

    def clean(self):
        if Contacts.objects.exists() and not self.pk:
            raise ValidationError(
                "You can only have one set of contact details")

    def save(self, *args, **kwargs):
        return super(Contacts, self).save(*args, **kwargs)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Contact Details'
        verbose_name_plural = 'Contact Details'


class Video(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    discount = models.IntegerField()
    slug = models.SlugField(unique=True, max_length=150)
    about = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    main_image = models.ImageField(upload_to="products", null=True)
    phone = models.CharField(max_length=16, blank=True, null=True, validators=[RegexValidator(
        regex='\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Nömrə düzgün formatda deyil")
    ])

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    image = models.ImageField(upload_to="products", null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')


class Sign(models.Model):
    icon = models.ImageField(upload_to='signs', null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=500)

    def __str__(self):
        return self.question


class ContactData(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(1000)
    phone = models.CharField(max_length=16, blank=True, null=True, validators=[RegexValidator(
        regex='\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Nömrə düzgün formatda deyil")
    ])

    def __str__(self):
        return self.full_name
