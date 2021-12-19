from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['some', 'text', 'or', 'massive', 'of', 'data', 'and', 'numbers', '1234567890'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
