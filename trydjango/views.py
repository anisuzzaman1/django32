from abc import get_cache_token
from django.http import HttpResponse # Website Response
#from articles.models import Article # Database Functions
from django.template.loader import render_to_string, get_template # Calling Template
from news.models import News

"""
To render of the web pages
"""

# Database binding /articles/models.py #
news_obj = News.objects.get(id=2)
news_tile = news_obj.title
news_content = news_obj.content
news_queryset = News.objects.all() # Get List of all from DB

# Django Templates /templates/home-view.html #
# HTML_STRING = render_to_string('home-view.html', context=context)

#  my_list = news_queryset # [102, 392, 233, 3954, 240]

# Using Dictionary
news_dictionary = {
    "object_list": news_queryset,
    "object": news_obj,
    "title": news_obj.title,
    "id": news_obj.id,
    "content": news_obj.content
}
# tmpl = get_template("home-view.html")
#tmpl_string = tmpl.render(context=news_dictionary)

HTML_STRING = render_to_string("home-view.html", context=news_dictionary)

# Website Body #
def home_view(request, id=None, *args, **kwargs):
    """
    Take in a request (Django send requests) 
    and return HTML as a return (We pick to return the request)
    """
    # print (100 * 1000)
    return HttpResponse(HTML_STRING)