from django.shortcuts import render
from .models import Liquidation
from django.http import HttpResponse

def dashboard(request):
# Get the latest 25 liquidations by order trade time in descending order
    liquidations = Liquidation.objects.order_by('-order_trade_time')[:25]
    context = {
    'liquidations': liquidations,
    }
    return render(request, 'liquidation_app/dashboard.html', context)

def about(request):
    return render(request, 'liquidation_app/about.html')

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'liquidation_app/contact.html', {'form': form})