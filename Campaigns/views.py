from django.shortcuts import render, get_object_or_404

from .models import Campaign

def detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    
    return render(request,'campaign/detail.html',{
        'Campaigns': campaign
    })
                  
