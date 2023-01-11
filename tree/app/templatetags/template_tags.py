from django import template

register = template.Library()

from ..models import Menu
@register.inclusion_tag('app/main_menu.html')
def draw_menu():
    main_menu = Menu.objects.all()
    menu = Menu.objects.all()
    return {'main_menu':main_menu, 'menu': menu}