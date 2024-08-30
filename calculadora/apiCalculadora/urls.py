from django.urls import path
from .views import SumaView, RestaView, MultiplicacionView, DivisionView

urlpatterns = [
    path('sumar', SumaView.as_view()),
    path('resta', RestaView.as_view()),
    path('multiplicacion', MultiplicacionView.as_view()),
    path('division', DivisionView.as_view())
]