from django.shortcuts import render,redirect
import requests
from .models import City
from .forms import CityForm
# Create your views here.
def home(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=7c97dcbd78bc46c88d37863b259231c7"

    err_msg=''
    message=''
    message_class=''
    count_collector=City.count_collector
    if request.method=='POST':
        form= CityForm(request.POST)

        if form.is_valid():
            new_city=form.cleaned_data['name']
            flag=0;
            for n in count_collector:
                if n==new_city:
                    flag=1;
                    count_collector.update({new_city:count_collector[new_city]+1})
            if flag==0:
                count_collector.update({new_city:1})

            existing_city_count=City.objects.filter(name=new_city).count()
            if existing_city_count==0:
                r=requests.get(url.format(new_city)).json()
                if r['cod']==200:
                    form.save()
                else:
                    err_msg='Invalid Location'
            else:
                err_msg='Location already exists in the database!'
        if err_msg:
            message= err_msg
            message_class='is-danger'
        else:
            message='Location Added Successfully'
            message_class='is-success'

    form = CityForm()

    cities= City.objects.all()

    weather_data=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
            'city': city.name,
            'temperature': round(r["main"]["temp"]-273.15,2),
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    weather_data=weather_data[::-1]
    count_collector=sorted(count_collector.items(),key=lambda x:x[1],reverse=True)
    return render(request,'weather/weather.html',{
                                                    'weather_data':weather_data,
                                                    'form':form,'message':message,
                                                    'message_class':message_class,
                                                    'count':count_collector,
                                                    })


def delete_city(request,city_name):
    del City.count_collector[city_name]
    City.objects.get(name=city_name).delete()
    return redirect('home')
