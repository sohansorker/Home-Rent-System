from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from houses.models import House
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



def flats(request, flat_id):
    flat = get_object_or_404(Flat, pk=flat_id)
    context = {
    'flat': flat
    }
    return render(request, 'listings/listing.html', context)



@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Home_owner').exists())
def addflats(request):
    if request.method == 'POST':
        user = request.user
        home = request.POST['house']
        flattype = request.POST['flattype']
        flatnumber = request.POST['flatnumber']
        size = request.POST['size']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        garages = request.POST['garages']
        discription = request.POST['discription']
        price = request.POST['price']
        availability = request.POST['availability']
        mainimage=request.FILES["mainimage"]
        addflat = Flat(
            house_id = home,
            flat_type =flattype,
            price = price,
            status = availability,
            flatnumber = flatnumber,
            description = discription,
            bedrooms = bedrooms,
            bathrooms = bathrooms,
            garage = garages,
            sqft = size,
            photo_main = mainimage,
        )
        if "image01" in request.FILES:
            image01 = request.FILES["image01"]
            addflat.photo_1 = image01
        if "image02" in request.FILES:
            image02=request.FILES["image02"]
            addflat.photo_2 = image02
        if "image03" in request.FILES:
            image03=request.FILES["image02"]
            addflat.photo_3 = image03
        if "image04" in request.FILES:
            image04=request.FILES["image04"]
            addflat.photo_4 = image04
        if "image05" in request.FILES:
            image05=request.FILES["image05"]
            addflat.photo_5 = image05
        if "image06" in request.FILES:
            image06=request.FILES["image06"]
            addflat.photo_6 = image06
        addflat.save()
        messages.success(request, 'Your New Flat Successfully Added')
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'This is not right way')
        return redirect('index')




def search(request):
    pass