from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from Campaigns.models import Campaign

@login_required
def index(request):
    campaigns = Campaign.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'campaigns': campaigns,
    })
