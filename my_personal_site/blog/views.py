import json

from typing import Any

# from datetime import date
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from .forms import CommentForm
from .models import Comment, Post


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-date')[:3]

# def index(request: HttpRequest) -> HttpResponse:
#     latest_posts = Post.objects.all().order_by('-date')[:3]
#     # latest_posts = sorted(posts_data, key=lambda post: post['date'], reverse=True)[:3]
#     return render(request, 'blog/index.html', {'posts': latest_posts})


class PostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = '-date'

# def posts(request: HttpRequest) -> HttpResponse:
#     all_posts = Post.objects.all().order_by('-date')
#     # all_posts = sorted(posts_data, key=lambda post: post['date'], reverse=True)
#     return render(request, 'blog/posts.html', {'posts': all_posts})


class PostView(View):

    def __is_stored(self, request: HttpRequest, id: int) -> bool:
        try:
            stored_posts_serialized: str = request.session['stored-posts']
        except KeyError:
            stored_posts = []
        else:
            stored_posts: list = json.loads(stored_posts_serialized)

        return id in stored_posts

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        post = Post.objects.get(slug=slug)
        is_saved_for_later = self.__is_stored(request, post.pk)
        form = CommentForm()
        return render(
            request, 'blog/post.html', {'post': post, 'form': form, 'comments': post.comments.all().order_by('-id'),
                                        'saved_for_later': is_saved_for_later})

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        post = Post.objects.get(slug=slug)
        is_saved_for_later = self.__is_stored(request, post.pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment: Comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post', args=(slug,)))

        return render(
            request, 'blog/post.html', {'post': post, 'form': form, 'comments': post.comments.all().order_by('-id'),
                                        'saved_for_later': is_saved_for_later})

# class PostView(DetailView):
#     model = Post
#     template_name = 'blog/post.html'
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['form'] = CommentForm()
#         return context


# def post(request: HttpRequest, slug: str) -> HttpResponse:
#     specific_post = get_object_or_404(Post, slug=slug)
#     # specific_post = next(post for post in posts_data if post['slug'] == slug)
#     return render(request, 'blog/post.html', {'post': specific_post})


class SaveForLaterView(View):

    def post(self, request: HttpRequest) -> HttpResponse:

        try:
            stored_posts_serialized: str = request.session['stored-posts']
        except KeyError:
            stored_posts = []
        else:
            stored_posts: list = json.loads(stored_posts_serialized)

        post_id = int(request.POST['post_id'])

        if post_id in stored_posts:
            stored_posts.remove(post_id)
        else:
            stored_posts.append(post_id)

        request.session['stored-posts'] = json.dumps(stored_posts)

        return HttpResponseRedirect(reverse('index'))

    def get(self, request: HttpRequest) -> HttpResponse:
        try:
            stored_posts_serialized: str = request.session['stored-posts']
        except KeyError:
            stored_posts = []
        else:
            stored_posts: list = json.loads(stored_posts_serialized)

        posts = Post.objects.filter(pk__in=stored_posts)

        return render(request, 'blog/stored-posts.html', {'posts': posts})


# class StoredPostsView(ListView):
#     model = Post
#     template_name = 'blog/stored-posts.html'
#     # context_object_name = 'posts'

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["posts"] = self.request.session.get('stored-posts')
#         return context
