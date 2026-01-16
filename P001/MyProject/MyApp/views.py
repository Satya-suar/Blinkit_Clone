from django.shortcuts import render

# Create your views here.
def wish_message(request):
    context={
        'message':'Welcome to Reciepe App'
    }
    return render(request,'home.html', context)