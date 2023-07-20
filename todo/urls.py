from django.urls import path
from . import views

urlpatterns = [
    # blank means home page.
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete')
]
