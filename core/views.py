from django.shortcuts import render
from .models import Caroussel,Mission,Apropos, Profile



def home_view(request):
    carousels = Caroussel.objects.filter(actif=True).order_by('ordre', 'date_creat')
    missions  = Mission.objects.filter(actif=True).order_by('position', 'date_creat')
    context = {
        'carousels': carousels,
        'missions':  missions,
    }
    return render(request,'core/home_page.html',context)


def apropos_page(request):
    appropos = Apropos.objects.first()
    context = {
        'appropos':appropos,
        'evenements':appropos.evenements.all(),
        'membres':appropos.profiles.all()
    }
    return render(request,'core/apropos_page.html',context)

def communaute_page(request):
    membres = Profile.objects.filter(role='membre').order_by('ordre')
    context = {
        'membres': membres,
    }
    return render(request, 'core/communaute_page.html', context)

def contact_page(request):
    return render(request,'core/contact_page.html')