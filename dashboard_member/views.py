from .models import BorrowActivity
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def member_dashboard(request):
    user = request.user
    borrow_activities = BorrowActivity.objects.filter(user=user)
    
    context = {
        'user': user,
        'borrow_activities': borrow_activities,
    }
    return render(request, 'member_dashboard.html', context)
