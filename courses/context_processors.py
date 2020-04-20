from courses.models import Category, MasterCategory


def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def master_categories_processor(request):
    master_categories = MasterCategory.objects.all()
    return {'master_categories': master_categories}
