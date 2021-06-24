from django.shortcuts import redirect, render
from .models import Reservation
from flats.models import Flat
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime

@login_required()
@user_passes_test(lambda u: u.groups.filter(name='user').exists())
def contact(request):
    if request.method == 'POST':
        flat_id = request.POST['flat_id']
    #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_reserved = Reservation.objects.all().filter(flat_id=flat_id, guest_id=user_id)
            if has_reserved:
                messages.error(request, 'You have already rent this flat')
                return redirect('/flats/'+flat_id)
        flat_object = Flat.objects.all().get(id=flat_id)  
        user_object = CustomUser.objects.all().get(id=user_id)
        check_in = request.POST['check_in_month']
        check_out = request.POST['check_out_month']
        dateformate = "%Y-%m"
        checkin = datetime.strptime(str(check_in), dateformate)
        checkout = datetime.strptime(str(check_out), dateformate)
        if checkout < checkin:
            messages.error(request, 'Invalid Month Selection')
            return redirect('/flats/'+flat_id)
        delta = (checkout.year - checkin.year) * 12 + (checkout.month - checkin.month)
        pricepermonth = int(request.POST['pricepermonth'])
        total_price = delta * pricepermonth
        father_name = request.POST['fathername']
        mother_name = request.POST['mothername']
        nationality = request.POST['nationality']
        nid = request.POST['nid']
        marital_status = request.POST['maritalstatus']
        reservation = Reservation(check_in=check_in, check_out=check_out, guest=user_object, flat=flat_object, paymentStatus='3',
        amount=total_price, father_name=father_name, mother_name=mother_name, nationality=nationality, nid=nid, marital_status=marital_status)
        reservation.save()
        Flat.objects.filter(id=flat_id).update(rent_status=False)
        messages.success(request, 'Your request has been submitted, Verify Your details and make the Payment')
        return redirect('/flats/'+flat_id)




@login_required()
@user_passes_test(lambda u: u.groups.filter(name='user').exists())
def makepayment(request):
    if 'bkash_number' in request.POST:
        reservationid = request.POST['reservationid']
        reservation = Reservation.objects.filter(id=reservationid)
        bkash_number = request.POST['bkash_number']
        trx = request.POST['trx']
        reservation.update(payment_number=bkash_number, trxid=trx, paymentStatus='1')
        messages.success(request,"Your payment has been added successfully")
        return redirect('userdash')
    else:
        reservationid = request.POST['reservationid']
        reservation = Reservation.objects.get(id=reservationid)
        context = {
            'reservation':reservation
        }
        return render(request,'dashboard/payments.html', context)