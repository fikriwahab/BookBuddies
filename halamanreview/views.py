from django.shortcuts import render

# Create your views here.
def show_reviewbuku(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "reviewbuku.html", context)