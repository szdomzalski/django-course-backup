from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'{self.full_name()}, {self.email}'


class Tag(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f'Tag "{self.caption}"'


class Post(models.Model):
    title = models.CharField(max_length=64)
    excerpt = models.CharField(max_length=256)
    # image_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images', null=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, default='', null=False, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self) -> str:
        return f'Post {self.title}, author: {self.author.first_name} {self.author.last_name}'


class Comment(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content
