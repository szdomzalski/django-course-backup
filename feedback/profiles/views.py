from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from .forms import ProfileForm
from .models import UserProfile


# Create your views here.
# def store_file(file: UploadedFile) -> None:
#     with open(f'temp/{file.name}', 'wb+') as f:
#         for chunk in file.chunks():
#             f.write(chunk)


class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    fields = '__all__'
    success_url = reverse_lazy('create-profile')


# class CreateProfileView(View):
#     def get(self, request: HttpRequest) -> HttpResponse:
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {'form': form})

#     def post(self, request: HttpRequest) -> HttpResponse:
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # store_file(request.FILES['image'])
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect(reverse('profiles'))
#         return render(request, "profiles/create_profile.html", {'form': form})


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profiles.html'
    context_object_name = 'profiles'
