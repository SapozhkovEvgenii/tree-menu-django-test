from django import template
from django.shortcuts import get_object_or_404
from tree_menu.models import TreeMenu
from django.core.exceptions import ObjectDoesNotExist


register = template.Library()


@register.inclusion_tag('tree_menu/tree_menu_tag.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(TreeMenu, name=menu_name)
    context['menu'] = menu
    current_url = context['request'].path
    try:
        current_menu = TreeMenu.objects.get(url=current_url)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_item_ids = current_menu.get_parents() + [current_menu.id]  # type: ignore
        context['unwrapped_menu_item_ids'] = unwrapped_menu_item_ids  # type: ignore

    return context


@register.inclusion_tag('tree_menu/tree_menu_tag.html', takes_context=True)
def draw_menu_children(context, menu_item_id):
    menu_item = get_object_or_404(TreeMenu, pk=menu_item_id)
    context['menu'] = menu_item
    return context
