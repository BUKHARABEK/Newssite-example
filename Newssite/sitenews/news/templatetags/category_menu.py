from django import template
from news.models import Category

register = template.Library()


@register.inclusion_tag('news/category_menu.html')
def show_category_menu(category_menu='dropdown-item'):
    categories = Category.objects.all()
    return {"categories": categories, "category_menu": category_menu}
