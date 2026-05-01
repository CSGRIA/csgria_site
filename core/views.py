from django.shortcuts import render, get_object_or_404
from .models import Caroussel, Mission, Apropos, Pole, Profile


def home_view(request):
    carousels = Caroussel.objects.filter(actif=True).order_by('ordre', 'date_creat')
    missions  = Mission.objects.filter(actif=True).order_by('position', 'date_creat')
    premiere_slide = carousels.first()
    return render(request, 'core/home_page.html', {
        'carousels': carousels,
        'missions':  missions,
        'premiere_slide': premiere_slide,
    })


def apropos_page(request):
    appropos = Apropos.objects.first()
    poles    = Pole.objects.filter(actif=True).prefetch_related('axes', 'membres')
    return render(request, 'core/apropos_page.html', {
        'appropos':   appropos,
        'evenements': appropos.evenements.all() if appropos else [],
        'membres':    appropos.profiles.all()   if appropos else [],
        'poles':      poles,
    })


def contact_page(request):
    return render(request, 'core/contact_page.html')

def communaute_page(request):
    membres = Profile.objects.filter(role='membre').order_by('ordre')
    context = {
        'membres': membres,
    }
    return render(request, 'core/communaute_page.html', context)


def pole_detail(request, slug):
    pole = get_object_or_404(Pole, slug=slug, actif=True)
    return render(request, 'core/pole_infos_page.html', {
        'pole':    pole,
        'axes':    pole.axes.all(),
        'membres': pole.membres.all(),
    })