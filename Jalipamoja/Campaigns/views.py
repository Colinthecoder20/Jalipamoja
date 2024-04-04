from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewCampaignForm, EditCampaignForm
from .models import Category, Campaign

def campaigns(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    campaigns = Campaign.objects.filter(is_closed=False)

    if category_id:
        campaigns = campaigns.filter(category_id=category_id)

    if query:
        campaigns = campaigns.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'campaign/campaigns.html', {
        'campaign': campaigns,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })
@login_required(login_url='/login/')
def detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    related_campaigns = Campaign.objects.filter(category=campaign.category, is_closed=False).exclude(pk=pk)[0:3]

    return render(request, 'campaign/detail.html', {
        'campaign': campaign,
        'related_campaigns': related_campaigns,
        
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewCampaignForm(request.POST, request.FILES)

        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user
            campaign.save()

            return redirect('campaign:detail', pk=campaign.id)
    else:
        form = NewCampaignForm()

    return render(request, 'campaign/form.html', {
        'form': form,
        'title': 'New campaign',
    })

@login_required
def edit(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditCampaignForm(request.POST, request.FILES, instance=campaign)

        if form.is_valid():
            form.save()

            return redirect('campaign:detail', pk=campaign.id)
    else:
        form = EditCampaignForm(instance=campaign)

    return render(request, 'campaign/form.html', {
        'form': form,
        'title': 'Edit campaign',
    })

@login_required
def delete(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk, created_by=request.user)
    campaign.delete()

    return redirect('dashboard:index')
                  
