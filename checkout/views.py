from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings



from .forms import OrderForm

def checkout(request):
    stripe_publish_key = settings.STRIPE_PUBLISH_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_publish_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

# Create your views here.
