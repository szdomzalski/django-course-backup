from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=32)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def get_absolute_url(self) -> str:
        return reverse("review-detail", kwargs={"pk": self.pk})

