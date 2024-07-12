from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from random import shuffle
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import Quote


@cache_page(60*120)
def index(request):
    quotes = Quote.objects.all()
    quotes_list = list(quotes)
    shuffle(quotes_list)
    cache.set("quotes_list", quotes_list, 60*120)
    current_quote = quotes_list[len(quotes_list)//2]
    return render(request, 'home/index.html', {"current_quote": current_quote})


def get_next_quote(request):
    cache_list = cache.get("quotes_list")

    quote_id = request.GET.get("quote_id")
    print("Quote id ", quote_id)
    index = -1

    for i, quote in enumerate(cache_list):
        print("for loop", quote_id, quote.id, quote_id==quote.id)
        if str(quote.id) == quote_id:
            print("Found quote on index", i)
            index = i
            break

    if index is len(cache_list)-1:
        current_quote = cache_list[0]
    else:
        current_quote = cache_list[index+1]

    print(current_quote.id, index, current_quote.text)

    quote_html = render_to_string("home/includes/quote.html", context={"current_quote": current_quote})
    return JsonResponse({"quote_html": quote_html, "quote_id": current_quote.id})



def get_previous_quote(request):
    cache_list = cache.get("quotes_list")

    quote_id = request.GET.get("quote_id")
    print("Quote id ", quote_id)
    index = -1

    for i, quote in enumerate(cache_list):
        print("for loop", type(quote_id), type(quote.id), quote_id==quote.id)
        if str(quote.id) == str(quote_id):
            print("Found quote on index", i)
            index = i
            break

    current_quote = cache_list[index-1]

    print(current_quote.id, index, current_quote.text)

    quote_html = render_to_string("home/includes/quote.html", context={"current_quote": current_quote})
    return JsonResponse({"quote_html": quote_html, "quote_id": current_quote.id})