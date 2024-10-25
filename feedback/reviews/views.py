from typing import Any

from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, FormView, ListView, TemplateView
# from django.views.generic.base import TemplateView
# from django.views.generic.edit import CreateView, FormView

from .forms import ReviewForm
from .models import Review


# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = reverse_lazy('thank-you')


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = reverse_lazy('thank-you')
#     # success_url = '/thank_you'

#     def form_valid(self, form: ModelForm) -> HttpResponse:
#         form.save()
#         return super().form_valid(form)


# class ReviewView(View):

#     def get(self, request: HttpRequest) -> HttpResponse:
#         form = ReviewForm()
#         return render(request, 'reviews/review.html', {'form': form})

#     def post(self, request: HttpRequest) -> HttpResponse:
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('thank-you'))

#         return render(request, 'reviews/review.html', {'form': form})


# def review(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         # existing_review = Review.objects.get(pk=1)
#         form = ReviewForm(request.POST)  # , instance=existing_review)
#         if form.is_valid():
#             # NOTE: Code below might be omitted if you've used ModelForm
#             # review = Review(username=form.cleaned_data['username'], text=form.cleaned_data['text'],
#             #                 rating=form.cleaned_data['rating'])
#             # review.save()
#             form.save()
#             return redirect(thank_you)
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/review.html', {'form': form})


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = 'Your opinion matters for us!'
        return context


# class ThankYouView(Temp):

#     def get(sekf, request: HttpRequest) -> HttpResponse:
#         return render(request, 'reviews/thank_you.html')

# def thank_you(request: HttpRequest) -> HttpResponse:
#     return render(request, 'reviews/thank_you.html')


class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     filtered_query = base_query.filter(rating__gt=3)
    #     return filtered_query


# class ReviewsListView(TemplateView):
#     template_name = 'reviews/review_list.html'

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["reviews"] = Review.objects.all()
#         return context


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review
    # context_object_name = 'review'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["favorite"] = int(self.request.session.get('favorite_review')) == self.object.id
        return context


# class ReviewDetailView(TemplateView):
#     template_name = 'reviews/review_detail.html'

#     def get_context_data(self, **kwargs) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["review"] = Review.objects.get(pk=kwargs['id'])
#         return context


class AddFavoriteView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect(reverse_lazy('review-detail', kwargs={'pk': review_id}))
