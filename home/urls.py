from django.urls import path, include

from .views import IndexView, ReceitaPDFView



urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('receitas/',ReceitaPDFView.as_view(), name='receita'),
    path('contas/', include('django.contrib.auth.urls')),
]
