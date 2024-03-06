from django import template
from news.models import *

register = template.Library()


@register.inclusion_tag('news/sidebar_popular_posts.html')
def get_popular(cnt=5):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('news/sidebar_categories.html')
def get_categories():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag('news/sidebar_tags.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}
