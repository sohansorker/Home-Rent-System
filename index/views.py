from django.shortcuts import render, HttpResponse
from flats.models import Flat
from houses.models import House
from django.contrib import messages
# Create your views here.
#homepage
def homepage(request):
    sflat = Flat.objects.order_by('-id').filter(rent_status=True)[:3]
    queryset_list = Flat.objects.order_by('-id')
    houseList = House.objects.order_by('-id')
    data = {
        'sflats':sflat,
        'flats': queryset_list,
        'houses':houseList,
    }
    response = render(request,'pages/index.html',data)
    return HttpResponse(response)


# about us page
def aboutpage(request):
    q = Flat.objects.all()
    return render(request, 'pages/about.html',{"data":q})



#contact page
def contactpage(request):
    return HttpResponse(render(request,'contact.html'))


# Search Page
def search(request):
    queryset_list = Flat.objects.order_by('-id').filter(rent_status=True)
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(house_id=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(house_id=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    houseList = House.objects.order_by('-id')
    context = {
    'flats': queryset_list,
    'houses':houseList,
    'values': request.GET
    }
    return render(request, 'listings/search.html', context)


