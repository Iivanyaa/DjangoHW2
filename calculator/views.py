from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def index(request):
    servings = request.GET.get('servings', 1)
    path = request.path
    context = {
        'recipes': {},
        'servings': servings,
        'path': path
    }
    for recipe in DATA.keys():
        context['recipes'][recipe] = DATA[recipe]
        for ingredient, serving in DATA[recipe].items():
            context['recipes'][recipe][ingredient] = DATA[recipe][ingredient]
    context['serving_times_servings'] = serving * servings

    return render(request, 'calculator/index.html', context)
