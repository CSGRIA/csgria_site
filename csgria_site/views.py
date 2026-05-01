from django.shortcuts import render




def construction_page(request):
    return render(request,'index.html')