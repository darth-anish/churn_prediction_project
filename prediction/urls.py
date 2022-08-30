from django.urls import path, include

from . import views

app_name = 'prediction'

urlpatterns=[
    path('',views.home,name='home'),
    path('features',views.show_significant_features,name='sig_features')
]