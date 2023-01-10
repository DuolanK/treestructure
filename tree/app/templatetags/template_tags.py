from django import template

register = template.Library()

from ..models import Employee
@register.inclusion_tag('app/main_menu.html')
def draw_menu():
    main_menu = Employee.objects.all()
    return {'main_menu': main_menu}