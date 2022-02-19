
from urllib.parse import urlencode

from django.shortcuts import render
from django.views import View

from orders.forms import NewOrderForm

import logging
import requests

logger = logging.getLogger(__name__)

# Create your views here.
class NewOrder(View):
    form_class = NewOrderForm

    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(request, 'orders/new.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        order_number = form['order_number'].value()
        logger.info("A request has been received to create the order: %s", order_number)

        # API Cal lto warehouse
        payload = {
            'order_number': order_number
        }
        r = requests.post("http://warehouse:9000/api/orders/", data=payload)

        # View context
        ctx = {
            'warehouse_success': r.status_code == requests.codes.ok,
            'order_number': order_number
        }

        logger.info("Warehouse responded with %s for %s: %s", r.status_code, order_number, r.json())

        return render(request, 'orders/new.html', ctx)