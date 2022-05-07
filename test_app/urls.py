from django.urls import path


from . import views

urlpatterns = [
    path("datetime/", views.DateDimeView.as_view()),
    path("random/", views.RandomNumView.as_view()),
]
