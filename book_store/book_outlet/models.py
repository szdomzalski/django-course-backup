from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
# from django.utils.text import slugify


# Create your models here.
class Country(models.Model):

    name = models.CharField(max_length=64)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f'{self.name} [{self.code}]'

    class Meta:
        verbose_name_plural = 'Countries'


class Address(models.Model):

    street = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.postal_code} {self.city}, {self.street}'

    class Meta:
        verbose_name_plural = 'Addresses'


class Author(models.Model):

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.full_name()


class Book(models.Model):

    title = models.CharField(max_length=64)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, related_name='books')

    def get_absolute_url(self) -> str:
        return reverse("book-detail", args=(self.slug,))

    # def save(self, *args, **kwargs) -> None:
    #     self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} ({self.rating})'
