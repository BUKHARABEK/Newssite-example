from django import template
from news.models import *

register = template.Library()


@register.inclusion_tag('news/home_popular_news.html')
def popular_news(cnt=5):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('news/home_latest_news.html')
def latest_news(cnt=3):
    posts = Post.objects.order_by('-time_create')[:cnt]
    return {"posts": posts}
