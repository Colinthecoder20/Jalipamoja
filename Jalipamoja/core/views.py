from django.shortcuts import render, redirect

from Campaigns.models import Category, Campaign


from .forms import SignupForm

def index(request):
    campaigns = Campaign.objects.filter(is_closed=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html',{
        'categories': categories,
        'campaigns': campaigns,
    })
        



def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:    
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })
    
from django.shortcuts import render, redirect
from .forms import LogoutForm

def logout_view(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout(request)
            return redirect('login')
    else:
        form = LogoutForm()
    return render(request, 'core/logout.html', {'form': form})    
       
   