from django.shortcuts import render

def home_page(request):
    return render(request, "todoapp_pages/home_page.html")
