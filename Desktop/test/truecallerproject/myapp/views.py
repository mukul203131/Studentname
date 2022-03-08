from django.shortcuts import render
from .models import Number
import phonenumbers
from phonenumbers import carrier,geocoder
# Create your views here.
def index(request):
    data = {}
    if request.method == "POST":
        number = request.POST['pnumber']
        a = Number(phone_number=number)
        a.save()
        p_number = phonenumbers.parse(number,None)
        coun =geocoder.description_for_number(p_number,'en')
        ser_provider=carrier.name_for_number(p_number,'en')
        data['country'] = coun
        data['sim_provider'] = ser_provider
        data['number'] =  p_number
    return render(request,'index.html',data)