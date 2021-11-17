from django.shortcuts import render
from .models import News
from news.form import NewsForms
from django.contrib.auth.decorators import login_required

def news_search_view(request):
    # print(request.GET)
    query_dict = request.GET # This is Query Dictionary
    query = query_dict.get("q")
    try:
        query = int(query_dict.get("q")) # Get only Int type
    except:
        query = None # Empty Query
    news_object = None
    if query is not None:
        news_object = News.objects.get(id=query)
    context = {
        "object": news_object
    }
    return render(request, "news/search.html", context=context)

def news_detail_view(request, id=None):
    news_object = None
    if id is not None:
        news_object = News.objects.get(id=id)
    context={
        "object": news_object,
    }
    return render(request, "news/detail.html", context=context)

# Module for Create # New Version
@login_required # Login Required Decorator
def news_create_view(request):
    form = NewsForms(request.POST or None)
    context = {
        "form": form 
    }
    if form.is_valid():
        news_obj = form.save()
        context['form'] = NewsForms()
        #context['object'] = news_obj
        #context['created'] = True
    return render(request, "news/create.html", context=context)