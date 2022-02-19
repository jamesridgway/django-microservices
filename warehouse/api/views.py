
from urllib.parse import urlencode

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import logging

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
class CreateOrder(View):

    def post(self, request):
        order_number = request.POST['order_number']
        logger.info("The order '%s' has been created in the warehouse system.", order_number)
        data = {
            'order_number': order_number
        }
        response_code = 500 if order_number.lower().startswith('f') else 200
        return JsonResponse(data, status=response_code)
