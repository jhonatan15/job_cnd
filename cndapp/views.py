from django.shortcuts import render

# Create your views here.
def cnd_app(request):
    return render(request, 'cndappinf/cndinfo.html', {})
