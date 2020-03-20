from .models import PageInfo

def info_processor(request):
    pageInfo = PageInfo.objects.all()
    if len(pageInfo):
        pageInfo = pageInfo[0]
    return {'pageInfo': pageInfo}
