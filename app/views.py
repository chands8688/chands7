from django.shortcuts import render

# Create your views here.
def condition(request):
    d1={'a':69}
    return render(request,'mj.html',d1)