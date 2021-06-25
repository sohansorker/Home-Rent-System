from django.shortcuts import render
from reservations.models import Reservation
from houses.models import House
from flats.models import Flat
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



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


@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Home_owner').exists())
def render_pdf_view(request):
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
    template_path = 'dashboard/report.html'
    context = {
        'user': user,
        'houses':houses,
        'houses_length':len(houses),
        'flats':totall_flats,
        'flats_length':flats_length,
        'available_flats':available_flats,
        'length_available_flats':len(available_flats),
        'reserved':total_reserved,
        'reserved_length':len(total_reserved), 
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response