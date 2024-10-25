from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    # Slug is a concept for search engine friendly subpages; can only have alphanumeric characters and hyphens
    path('posts/<slug:slug>', views.PostView.as_view(), name='post'),
    path('save-for-later', views.SaveForLaterView.as_view(), name='save-for-later'),
]
