from django.shortcuts import render


def all_menu(request, url=None):
    return render(request, 'tree_menu/menu.html')
