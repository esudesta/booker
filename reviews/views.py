from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return  render(request,"reviews/index.html",context)
def search_view(request):
    # context = {

    # }
    pass