from django import template

register = template.Library()

from ..models import Menu
@register.inclusion_tag('app/main_menu.html')
def draw_menu():
    main_menu = Menu.objects.filter(category='PRT')
    menu = Menu.objects.filter(category='CHD')
    return {'main_menu':main_menu, 'menu':menu}


@register.inclusion_tag('app/prop_menu.html')
def menu_menu():
    main_menu = Menu.objects.filter(category='PRT')
    menu = Menu.objects.filter(category='CHD')
    return {'main_menu':main_menu, 'menu':menu}