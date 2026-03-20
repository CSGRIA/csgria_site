from django.shortcuts import render




def home_view(request):
    
    return render(request,'core/home_page.html')


def apropos_page(request):
    return render(request,'core/apropos_page.html')

def contact_page(request):
    return render(request,'core/contact_page.html')