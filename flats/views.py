from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Flat

def index(request):
    sflat = Flat.objects.order_by('-id').filter(rent_status=True)

    paginator = Paginator(sflat, 6)
    page = request.GET.get('page')
    paged_flats = paginator.get_page(page)

    context = {
      'sflats': paged_flats
    }

    return render(request, 'listings/listings.html', context)



def flats(request):
    pass


def search(request):
    pass