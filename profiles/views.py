from django.shortcuts import render

# Create your views here.

def profile(request):
    """
    Display the users profie
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
