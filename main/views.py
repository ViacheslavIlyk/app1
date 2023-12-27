from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'CORPS - Головна',
        'content': 'Магазин меблів CORPS'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'CORPS - Про нас',
        'content': 'Про нас',
        'text_on_page': 'Текст про то, чому цей магазин такий класний, а товар на ньому дуже якісний'
    }
    return render(request, 'main/about.html', context)



