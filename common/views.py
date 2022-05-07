from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View



class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        hello = "<h1>Hello, World</h1>"

        return HttpResponse(hello)

class IndexView(View):
    def get(self, request: HttpRequest):
       return render(request, 'common/index.html')

