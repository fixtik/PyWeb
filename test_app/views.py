from datetime import datetime
from random import random

from django.views import View
from django.http import HttpRequest, HttpResponse



class DateDimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)

class RandomNumView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        num = random()

        return HttpResponse(num)


# Create your views here.
