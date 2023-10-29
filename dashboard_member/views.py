from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MemberLoanActivity

@login_required
def member_dashboard(request):
    user = request.user
    member_loans = MemberLoanActivity.objects.filter(user=user)

    context = {
        'user': user,
        'member_loans': member_loans,
    }

    return render(request, 'dashboard_member/dashboard_member.html', context)
