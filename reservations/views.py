from django.shortcuts import redirect
from .models import Reservation
from flats.models import Flat
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


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
        payment_number = request.POST['bkashbumber']
        trxid = request.POST['trxid']
        amount = request.POST['sendamount']
        father_name = request.POST['fathername']
        mother_name = request.POST['mothername']
        nationality = request.POST['nationality']
        nid = request.POST['nid']
        marital_status = request.POST['maritalstatus']
        reservation = Reservation(check_in=check_in, check_out=check_out, guest=user_object, flat=flat_object, payment_number=payment_number,
        trxid=trxid, amount=amount, father_name=father_name, mother_name=mother_name, nationality=nationality, nid=nid, marital_status=marital_status)
        reservation.save()
        Flat.objects.filter(id=flat_id).update(rent_status=False)
        messages.success(request, 'Your request has been submitted, we will approved your order after virify all details')
        return redirect('/flats/'+flat_id)