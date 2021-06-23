from django.shortcuts import render
from reservations.models import Reservation
from houses.models import House
from flats.models import Flat
from django.contrib.auth.decorators import login_required, user_passes_test



# Create your views here.
@login_required()
@user_passes_test(lambda u: u.groups.filter(name='user').exists())
def userdash(request):
    user = request.user.id
    reservation = Reservation.objects.order_by('-id').filter(guest_id = user)
    context = {
        'reservation':reservation,
    }
    return render(request, 'dashboard/userdash.html', context)



@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Home_owner').exists())
def hodash(request):
    user = request.user
    houses = House.objects.filter(owner=user)
    totall_flats = []
    total_reserved = []
    for house in houses:
        flats = Flat.objects.filter(house=house)
        for flat in flats:
            reserved = Reservation.objects.order_by('-id').filter(flat=flat)
            total_reserved += reserved
        totall_flats += flats           
    flats_length = len(totall_flats)
    available_flats = Flat.objects.filter(rent_status=True)
    context = {
        'houses':houses,
        'houses_length':len(houses),
        'flats':totall_flats,
        'flats_length':flats_length,
        'available_flats':available_flats,
        'length_available_flats':len(available_flats),
        'reserved':total_reserved,
        'reserved_length':len(total_reserved),

    }
    return render(request, 'dashboard/hodash.html', context)