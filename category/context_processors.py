from .models import Category


def Categories(request):
    category_options = Category.objects.all()
    context = {
        'category_options':category_options,
    }

    return dict(context)