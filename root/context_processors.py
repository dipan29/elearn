from .models import PageInfo

def info_processor(request):
    pageInfo = PageInfo.objects.all()[0]
    return {'pageInfo': pageInfo}
