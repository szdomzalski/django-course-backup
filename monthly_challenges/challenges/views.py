from django.http import Http404, HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': 'This is January challenge view.',
    'february': 'This is February challenge view.',
    'march': 'This is March challenge view.',
    'april': 'This is April challenge view.',
    'may': 'This is May challenge view.',
    'june': 'This is June challenge view.',
    'july': 'This is July challenge view.',
    'august': 'This is August challenge view.',
    'september': 'This is September challenge view.',
    'october': 'This is October challenge view.',
    'november': 'This is November challenge view.',
    # 'december': 'This is December challenge view.',
    'december': None,
}


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # pages = ''
    # for month in monthly_challenges.keys():
    #     pages += f'<li><a href="{reverse('month-challenge', args=(month,))}">{month.capitalize()}</a></li>'
    # response = f'<h2><ul>{pages}</ul></h2>'
    # return HttpResponse(response)
    return render(request, 'challenges/index.html', {'months': monthly_challenges.keys()})


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    try:
        forward_month = [*monthly_challenges.keys()][month - 1]
        forward_url = reverse('month-challenge', args=(forward_month,))
    except IndexError:
        # error_respomse = render_to_string('404.html')
        # return HttpResponseNotFound(error_respomse)
        raise Http404()
    else:
        # return redirect(monthly_challenge, forward_month)
        return HttpResponseRedirect(forward_url)


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    try:
        response = monthly_challenges[month.lower()]
    except KeyError:
        # error_respomse = render_to_string('404.html')
        # return HttpResponseNotFound(error_respomse)
        raise Http404()
    else:
        # return HttpResponse(render_to_string('challenges/challenge.html'))
        return render(request, 'challenges/challenge.html', {'month': month, 'challenge': response})
