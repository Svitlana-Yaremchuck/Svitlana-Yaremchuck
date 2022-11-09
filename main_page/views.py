from django.shortcuts import render
from .models import Category, Dish

# Create your views here.

def main_view(request):

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    specials = Dish.objects.filter(is_visible=True, is_special=True)

    return render(request, 'base.html', context={
        'categories': categories,
        'dishes': dishes,
        'specials': specials,

    })

