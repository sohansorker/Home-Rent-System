from django.shortcuts import render, redirect, get_object_or_404
from reservations.models import Reservation
from houses.models import House
from flats.models import Flat
from django.contrib import messages
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
@user_passes_test(lambda u: u.groups.filter(name='user').exists() or u.groups.filter(name='Home_owner').exists())
def cancelorder(request):
    if request.method == 'POST':
        id = request.POST['reservationid']
        order = Reservation.objects.get(id=id)
        flat = Flat.objects.filter(id=order.flat_id)
        flat.update(rent_status=True)
        Reservation.objects.filter(id=id).delete()
        messages.success(request,"Reservation Canceled Successfully")
        return redirect(request.META['HTTP_REFERER'])



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
def changestatus(request):
    if request.method == 'POST':
        reservation = Reservation.objects.filter(id = request.POST['reservationid'])
        if 'policeStatus' in request.POST:
            reservation.update(policeStatus = request.POST['policeStatus'])
        if 'paymentStatus' in request.POST:
            reservation.update(paymentStatus = request.POST['paymentStatus'])
        if 'status' in request.POST:
            reservation.update(status = request.POST['status'])

        messages.success(request,"Status Updated Successfully")
        return redirect(request.META['HTTP_REFERER']) 



@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Home_owner').exists())
def vieworder(request, flat_id):
    reservation = Reservation.objects.filter(flat_id=flat_id).first()
    if reservation:
        context = {
            'reservation' : reservation,
        }
        return render(request,'dashboard/vieworder.html', context)
    else:
        messages.success(request,"It's Not Booked Yet")
        return redirect(request.META['HTTP_REFERER'])



@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Home_owner').exists())
def editflat(request, flat_id):
    flat = get_object_or_404(Flat, pk=flat_id)
    context = {
    'flat': flat,
    }
    return render(request, 'dashboard/editflat.html', context)



@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Home_owner').exists())
def editflats(request):
    if request.method == 'POST':
        flat = Flat.objects.filter(id = request.POST['flatid'])
        if 'flatnumber' in request.POST:
            flat.update(flatnumber = request.POST['flatnumber'])
        if 'flattype' in request.POST:
            flat.update(flat_type = request.POST['flattype'])
        if 'price' in request.POST:
            flat.update(price = request.POST['price'])
        if 'status' in request.POST:
            flat.update(status = request.POST['status'])
        if 'bedrooms' in request.POST:
            flat.update(bedrooms = request.POST['bedrooms'])
        if 'bathrooms' in request.POST:
            flat.update(bathrooms = request.POST['bathrooms'])
        if 'garage' in request.POST:
            flat.update(garage = request.POST['garage'])
        if 'size' in request.POST:
            flat.update(sqft = request.POST['size'])
        if 'description' in request.POST:
            flat.update(description = request.POST['description'])
        if 'image' in request.FILES:
            flat.update(photo_main = request.POST['image'])
        
        messages.success(request,"Status Updated Successfully")
        return redirect(request.META['HTTP_REFERER'])




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