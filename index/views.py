from django.shortcuts import render, HttpResponse
from houses.models import House
from flats.models import Flat
from reservations.models import Reservation
from django.contrib import messages
# Create your views here.
#homepage
def homepage(request):
    # all_location = House.objects.values_list('location','id').distinct().order_by()
    sflat = Flat.objects.order_by('-id').filter(rent_status=True)[:3]
    # if request.method =="POST":
    #     try:
    #         house = House.objects.all().get(id=int(request.POST['search_location']))
    #         rr = []
    #         #for finding the reserved rooms on this time period for excluding from the query set
    #         for each_reservation in Reservation.objects.all():
    #             if str(each_reservation.check_in) < str(request.POST['cin']) and str(each_reservation.check_out) < str(request.POST['cout']):
    #                 pass
    #             elif str(each_reservation.check_in) > str(request.POST['cin']) and str(each_reservation.check_out) > str(request.POST['cout']):
    #                 pass
    #             else:
    #                 rr.append(each_reservation.room.id)
    #         room = Flat.objects.all().filter(house=house,capacity__gte = int(request.POST['capacity'])).exclude(id__in=rr)
    #         if len(room) == 0:
    #             messages.warning(request,"Sorry No Flats Are Available on this time period")
    #         check_in = request.POST['cin']
    #         check_out = request.POST['cout']
    #         data = {'rooms':room,'sflats':sflat,'all_location':all_location,"cin":check_in, "cout":check_out, 'flag':True}
    #         response = render(request,'pages/index.html',data)
    #     except Exception as e:
    #         messages.error(request,e)
    #         response = render(request,'pages/index.html',{'sflats':sflat,'all_location':all_location})
    # else: 
    data = {'sflats':sflat}
    response = render(request,'pages/index.html',data)
    return HttpResponse(response)


# about us page
def aboutpage(request):
    q = Flat.objects.all()
    return render(request, 'pages/about.html',{"data":q})



#contact page
def contactpage(request):
    return HttpResponse(render(request,'contact.html'))

