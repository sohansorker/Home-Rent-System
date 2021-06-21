from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import House



# Create your views here.
@login_required()
@user_passes_test(lambda u: u.groups.filter(name='Home_owner').exists())
def addhouse(request):
    if request.method == 'POST':
        user = request.user
        homename = request.POST['homename']
        location = request.POST['location']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        if "homeimage" in request.FILES:
            homeimage=request.FILES["homeimage"]
        addhouse = House(name=homename, owner=user, location=location, state=state, zipcode=zipcode, country=country, photo=homeimage)
        addhouse.save()
        messages.success(request, 'Your New House Successfully Added')
        return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'This is not right way')
        return redirect('index')