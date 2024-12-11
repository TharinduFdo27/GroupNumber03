from django.shortcuts import render
from .forms import InvestmentForm


def funding(request):
    return render(request, 'Funding.html')


def home(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InvestmentForm()

    investments = Investment.objects.all()
    total_investment = sum(i.investment_amount for i in investments)

    return render(request, 'Group_03_Home.html', {
        'form': form,
        'investments': investments,
        'total_investment': total_investment,
    })
